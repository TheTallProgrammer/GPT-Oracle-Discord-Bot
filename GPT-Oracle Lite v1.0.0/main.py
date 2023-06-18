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
import os
from gpt_driver import receive_input

intents = discord.Intents.all()
client = discord.Client(intents=intents)
is_first_message = True


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(f"Received a message from {message.author} in channel {message.channel}: {message.content}")
    try:
        global is_first_message
        
        # Avoid responding to ourselves
        if message.author == client.user:
            return
        if is_first_message:
            await message.channel.send('Just a heads up, this is a fresh instance of the bot, previous conversations have been forgotten!')
            is_first_message = False
        # Check if the message starts with the command prefix
        if not message.content.startswith('!'):
            return
        # Store the content of the message in a string, removing the command prefix 
        user_input = message.content[1:]

        # Extract api_key_file and question
        api_key_file, question = user_input.split(", ", 1)

        # Read the API key from the file
        try:
            with open(api_key_file, 'r') as file:
                api_key = file.read().strip()
        except Exception as e:
            await message.reply(f"Error reading API key file: {str(e)}\n Please try again.")
            return

        # Call GPT-3 with the API key and question
        try:
            for reply in receive_input(api_key, question):
                await message.reply(reply)
        except ValueError as e:
            await message.reply(str(e))
    except ValueError as e:
        await message.reply(str(e))



TOKEN = os.getenv('DISCORD_BOT_TOKEN')
client.run(TOKEN)
