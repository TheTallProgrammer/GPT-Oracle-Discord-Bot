# Copyright 2023 Logan Falkenberg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import required libraries
import discord
import asyncio
from gpt_driver import receive_input
from discord.ext import commands
from database import get_api_key, save_api_key
from concurrent.futures import ThreadPoolExecutor
from dalle_driver import receive_draw_input
import openai

# Create a ThreadPoolExecutor instance
executor = ThreadPoolExecutor()

# Set up all intents for bot
intents = discord.Intents.all()

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# This variable is used to track if the bot has sent its first message or not
bot.is_first_message = True

# This event is triggered when the bot has connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# This command saves the user's API key
@bot.command()
async def save_key(ctx, key):
    # Check if the command is used in a Direct Message
    if not isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send(f'{ctx.author.mention}, This command can only be used in a DM.')
        return
    # Validate the API key and save it if it's valid
    if validate_api_key():
        save_api_key(ctx.message.author.id, key)
        await ctx.send(f'{ctx.author.mention}, API key saved.')
    else:
        await ctx.send(f"{ctx.author.mention}, API Key Invalid.")

# This command allows the user to ask a question which the bot answers
@bot.command()
async def ask(ctx, *, question):
    api_key = get_api_key(ctx.message.author.id)
    if not api_key:
        await ctx.send(f"{ctx.author.mention}, No API key found for your account. Please save your API key using the !save_key command.")
        return
    try:
        # Check if this is the bot's first message
        if bot.is_first_message:
            await ctx.send("Attention all! This is a fresh instance of the bot, so previous conversations have been forgotten!")
            bot.is_first_message = False
        print(f"Received a message from {ctx.message.author} in channel {ctx.message.channel}: {ctx.message.content}")
        loop = asyncio.get_event_loop()
        typing_task = None
        try:
            # Show typing indicator
            typing_task = bot.loop.create_task(typing_indicator(ctx))
            replies = await loop.run_in_executor(executor, receive_input, api_key, question)
            for reply in replies:
                print(reply)
                mention = f"{ctx.author.mention}, "
                chunk_size = 2000 - len(mention)
                # Send the reply in chunks to avoid message limit
                for part in get_chunks(reply, limit=chunk_size):
                    await ctx.send(mention + part)
        except Exception as e:
            await ctx.send(f"{ctx.author.mention}, An error occurred: {str(e)}")
        finally:
            if typing_task:
                typing_task.cancel()
    except ValueError as e:
        await ctx.send(str(e))

# This command allows the bot to generate and send a drawing based on a user's request
@bot.command()
async def draw(ctx, *, question):
    api_key = get_api_key(ctx.message.author.id)
    if not api_key:
        await ctx.send(f"{ctx.author.mention}, No API key found for your account. Please save your API key using the !save_key command.")
        return
    try:
        print(f"{ctx.author} Entered: {question}")
        await ctx.send(receive_draw_input(api_key, question))
    except TimeoutError:
        await ctx.send(f"{ctx.author.mention}, The drawing prompt timed out. Please try again.")
    except ValueError as e:
        await ctx.send(str(e))

# Function to validate an API key
async def validate_api_key(api_key):
    try:
        # Attempt to list models with the API key
        openai.api_key = api_key
        openai.Model.list()
        return True
    except Exception:
        return None

# This function shows a typing indicator every 10 seconds
async def typing_indicator(ctx):
    while True:
        async with ctx.typing():
            await asyncio.sleep(10)

# This function breaks a message into chunks to avoid hitting the message limit
def get_chunks(message, limit):
    return [message[i:i+limit] for i in range(0, len(message), limit)]

# This event ensures bot commands are processed
@bot.event
async def on_message(message):
    await bot.process_commands(message)


TOKEN = 'TOKEN'
bot.run(TOKEN)
