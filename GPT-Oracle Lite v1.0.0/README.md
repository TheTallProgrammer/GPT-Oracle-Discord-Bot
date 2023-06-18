
<h1 align="center">🤖 GPT-Oracle Lite 🚀</h1>

<p align="center">An AI-driven chatbot for Discord using OpenAI's GPT 3.5 model, designed to handle user queries and responses in a natural, conversational manner.</p>


<h2 align="left">🌟 Features </h2>

- 🗣️ **AI Chatbot**: Utilizes the power of GPT-3.5-Turbo-16K, one of the most advanced language models, for real-time, dynamic conversations.
- 🎟️ **Token Count Limitation**: Ensures that the conversation stays within GPT-3's token limits, managing older conversations when the token limit is reached.
- 🛠️ **Customization**: Can be easily customized to perform a variety of tasks by changing the system message in the conversation initialization.
- 🔒 **Security**: The API key used for OpenAI's GPT-3 is read from a file, ensuring that it's not hardcoded into the bot's code and prevents others from seeing it in chat.
- 🗝️ **API Key Validation**: Validates the OpenAI API key before processing the user input. If the key is not valid, it notifies the user.
- 🚀 **Automatic Responses**: Sends an automatic message every time it is started, informing users that it's a fresh instance and previous conversations have been forgotten.
- 📝 **Intelligent Character Limit Handling**: The bot smartly handles Discord's 2000 character limit per message. If a response exceeds this limit, the bot splits the message and sends the remaining text in subsequent messages, ensuring you never miss any information due to Discord's character constraints.

<h2 align="left">📖 How It Works </h2>

The bot reads user messages that start with '!', followed by the path to the file containing the API key, and the question separated by a comma. For example: `!C:\Users\Name\Desktop\api_key.txt, What is the capital of France?`. 

On the first launch, the bot informs the users that it's a fresh instance and it does not remember previous conversations. As users ask questions, the bot calls the GPT-3 model to generate responses, which are sent back to the Discord channel.

The bot also keeps track of the token count in the conversation to ensure it doesn't exceed GPT-3's token limit. If the token count nears the limit, it removes the oldest conversation to free up tokens.


<h2 align="left">🚀 Usage </h2>

1. **Obtain Your OpenAI API Key:** GPT-Oracle Lite integrates with OpenAI's GPT model, necessitating an OpenAI API key for its operation. You can [create your OpenAI API key](https://platform.openai.com/account/api-keys) by registering a free account. Please be aware, the API key is displayed just once, so **ensure you save your API key to a local text file for future usage.** If misplaced, a new one will need to be generated.

2. **Get Your Discord Bot Token:** This requires creating a new application in the Discord developer portal, adding a bot to the application, and copying the bot's token. Full instructions can be found in the [Discord Developer Portal](https://discord.com/developers/docs/intro).

3. **Set Up Environment Variable:** To use this bot, you need to set the environment variable `DISCORD_BOT_TOKEN` to your Discord Bot token, which the bot uses to authenticate with the Discord API. Depending on your operating system, this process can vary:

   - **Windows:** You can use the `setx` command in your command prompt:
     ```
     setx DISCORD_BOT_TOKEN "your-token-here"
     ```

   - **Linux/Mac:** You can add it to your shell's configuration file (such as `~/.bashrc` or `~/.bash_profile`) with the following line:
     ```
     export DISCORD_BOT_TOKEN="your-token-here"
     ```

     > Note: If you're using an Integrated Development Environment (IDE) like PyCharm or Visual Studio Code, you might have to restart it for the new environment variable to take effect.

     You can then access this environment variable in your Python code using the `os` module (already in the source code):
     ```python
     import os

     TOKEN = os.getenv('DISCORD_BOT_TOKEN')
     ```

     > Remember not to include your actual bot token in your code or version control system. Always keep it separate and securely stored.


4. **Running the Bot:** In the current release, the bot can be started through the command line. Navigate to the directory containing the `main.py` file and run the bot using the following command:

     ```
     python main.py
     ```

    This will start the bot, and it will be ready to accept commands in your Discord server.

5. **Interacting with the Bot:** Now, provide your OpenAI API key file path and your question or message to the bot separated by a comma.

   - Example Input to the bot: "*C:\Users\Name\Desktop\api_key.txt, what is the most popular video game?*"


<h2 align="left">🔜 Upcoming: GPT-Oracle Plus </h2>

In the near future, I plan to release **GPT-Oracle Plus**. This upgrade will allow users to issue administrative commands to the bot, which the bot will then execute. For example, if a user were to input `!C:\Users\Name\Desktop\api_key.txt, change my nickname to Omniman`, GPT-Oracle Plus would not only generate a conversational response, but also determine if the user input includes a request for a command execution. If such a request is identified, the bot will change their nickname.

This upcoming feature is aimed at increasing interactivity and user control, effectively enabling GPT-Oracle Plus to serve as an intelligent, conversational, and command-executing assistant for Discord users. Stay tuned for updates! 


<h2 align="left">👨‍💻 Author </h2>

<div align="center">
  
 
  
  🔧 **Logan Falkenberg** - *Lead Developer*
  
  For any queries, discussions, or feedback, I am always open. Feel free to reach out:
  
  📧 **Email:** [loganf0101@gmail.com](mailto:loganf0101@gmail.com) 
  
  🌐 **GitHub:** [@TheTallProgrammer](https://github.com/TheTallProgrammer)
  
</div>


<h2 align="left">📜 License </h2>

<div align="center">
  
  This project is licensed under the terms of the Apache License 2.0. Please see [LICENSE](LICENSE) for more details.
  
  ![License Logo](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
  
</div>

