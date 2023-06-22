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
import discord
import asyncio
from gpt_driver import receive_input
from discord.ext import commands
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.is_first_message = True


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def save_key(ctx, key):
    if not isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send('This command can only be used in a DM.')
        return

    with open(str(ctx.message.author.id) + '_key.txt', 'w') as f:
        f.write(key)

    await ctx.send('API key saved.')


@bot.command()
async def ask(ctx, *, question):
    try:
        with open(str(ctx.message.author.id) + '_key.txt', 'r') as f:
            api_key = f.read().strip()
    except FileNotFoundError:
        await ctx.send(f"{ctx.author.mention}, No API key found for your account. Please save your API key using the !save_key command.")
        return

    if bot.is_first_message:
        await ctx.send("Attention all! This is a fresh instance of the bot, so previous conversations have been forgotten!")
        bot.is_first_message = False

    print(f"Received a message from {ctx.message.author} in channel {ctx.message.channel}: {ctx.message.content}")

    try:
        typing_task = bot.loop.create_task(typing_indicator(ctx))

        loop = asyncio.get_event_loop()
        try:
            replies = await loop.run_in_executor(executor, receive_input, api_key, question)
            for reply in replies:
                print(reply)
                mention = f"{ctx.author.mention}, "
                chunk_size = 2000 - len(mention)
                for part in get_chunks(reply, limit=chunk_size):
                    await ctx.send(mention + part)
        except Exception as e:
            await ctx.send(f"{ctx.author.mention}, An error occurred: {str(e)}")
        finally:
            typing_task.cancel()
    except ValueError as e:
        await ctx.send(str(e))


async def typing_indicator(ctx):
    while True:
        async with ctx.typing():
            await asyncio.sleep(5)  # Wait a bit before typing again


def get_chunks(message, limit):
    return [message[i:i+limit] for i in range(0, len(message), limit)]


@bot.event
async def on_message(message):
    # We add this to ensure our bot commands still get processed
    await bot.process_commands(message)


TOKEN = 'TOKEN'
bot.run(TOKEN)
