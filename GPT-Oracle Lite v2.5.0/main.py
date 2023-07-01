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
import asyncio
import aiofiles
import discord
from gpt_driver import receive_input
from discord.ext import commands
from concurrent.futures import ThreadPoolExecutor
from dalle_driver import receive_draw_input
import openai

# Create an executor for handling blocking IO tasks
executor = ThreadPoolExecutor()

intents = discord.Intents.all()

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)
bot.is_first_message = True

# Create a dictionary to store API keys in memory
api_keys = {}

# EVENT: When bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# COMMAND: Save API key
@bot.command()
async def save_key(ctx, key):
    # Ensure command is used in a direct message
    if not isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send('This command can only be used in a DM.')
        return
    # Validate API key
    if await validate_api_key(key):
        # Save key to a file
        async with aiofiles.open(f'{ctx.message.author.id}_key.txt', 'w') as f:
            await f.write(key)
        # Also store key in memory for faster access
        api_keys[ctx.message.author.id] = key
        await ctx.send(f'{ctx.author.mention}, API key saved.')
    else:
        await ctx.send(f"{ctx.author.mention}, Invalid API Key.")

# COMMAND: Ask a question
@bot.command()
async def ask(ctx, *, question):
    # Get the API key for the author of the message
    api_key = await get_api_key(ctx.message.author.id)
    if not api_key:
        await ctx.send(f"{ctx.author.mention}, No API key found for your account. Please save your API key using the !save_key command.")
        return
    if bot.is_first_message:
        await ctx.send("Attention all! This is a fresh instance of the bot, so previous conversations have been forgotten!")
        bot.is_first_message = False
    print(f"Received a message from {ctx.message.author} in channel {ctx.message.channel}: {ctx.message.content}")
    loop = asyncio.get_event_loop()
    # Create a task for showing the typing indicator
    typing_task = bot.loop.create_task(typing_indicator(ctx))
    try:
        # Run the receive_input function in the executor to avoid blocking the event loop
        replies = await loop.run_in_executor(executor, receive_input, api_key, question)
        for reply in replies:
            print(reply)
            mention = f"{ctx.author.mention}, "
            # Split the reply into chunks and send each one separately
            for part in get_chunks(reply, limit=2000-len(mention)):
                await ctx.send(mention + part)
    except Exception as e:
        await ctx.send(f"{ctx.author.mention}, An error occurred: {str(e)}")
    finally:
        # Ensure the typing indicator task is cancelled even if an error occurs
        typing_task.cancel()

# COMMAND: Draw something
@bot.command()
async def draw(ctx, *, question):
    api_key = await get_api_key(ctx.message.author.id)
    if not api_key:
        await ctx.send(f"{ctx.author.mention}, No API key found for your account. Please save your API key using the !save_key command.")
        return
    print(f"{ctx.author} Entered: {question}")
    try:
        # Run the receive_draw_input function
        await ctx.send(receive_draw_input(api_key, question))
    except TimeoutError:
        await ctx.send(f"{ctx.author.mention}, The drawing prompt timed out. Please try again.")
    except ValueError as e:
        await ctx.send(str(e))

# FUNCTIONS
# Function to retrieve API key from memory or file
async def get_api_key(author_id):
    if author_id in api_keys:
        return api_keys[author_id]
    try:
        async with aiofiles.open(f"{author_id}_key.txt", 'r') as f:
            return (await f.read()).strip()
    except FileNotFoundError:
        return None

# Function to validate an API key
async def validate_api_key(api_key):
    try:
        # Attempt to list models with the API key
        openai.api_key = api_key
        openai.Model.list()
        return True
    except Exception:
        return None

# Coroutine that sends a typing indicator every 10 seconds
async def typing_indicator(ctx):
    while True:
        async with ctx.typing():
            await asyncio.sleep(10)

# Function to split a message into chunks
def get_chunks(message, limit):
    for i in range(0, len(message), limit):
        yield message[i:i+limit]

# EVENT: Process every message received
@bot.event
async def on_message(message):
    await bot.process_commands(message)

# Retrieve the bot token from an environment variable
TOKEN = ''

# Run the bot
bot.run(TOKEN)
