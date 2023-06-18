<h1 align="center">🤖 GPT-Oracle Discord Bot 🚀</h1>

<p align="center">A powerful, AI-driven chatbot for Discord capable of delivering high-quality, interactive, and conversational experiences to users.</p>


<h2 align="left">🌟 Features </h2>

- 🗣️ **AI Chatbot**: Leverages the capabilities of advanced language models to facilitate real-time, engaging conversations.
- 🎟️ **Token Management**: Ensures smooth conversation flow by effectively managing token count within the permissible limits of the AI model.
- 🛠️ **Customizability**: Allows users to easily modify the bot's functionality for diverse tasks by altering the system message during conversation initiation.
- 🔒 **Security**: Prioritizes security by sourcing the AI model's API key from a file, preventing hardcoding in the bot's code and ensuring its invisibility in chats.
- 🗝️ **API Key Validation**: Validates the API key prior to processing user input. If the key is invalid, the user is promptly notified.
- 🚀 **Automatic Responses**: Sends an automated message every time it is launched, notifying users of its status as a fresh instance with no recollection of previous conversations.
- 📝 **Smart Character Limit Management**: Effectively manages Discord's 2000 character limit per message. If a response surpasses this limit, the bot splits the message and sends the remainder in subsequent messages, ensuring no loss of information due to character constraints.

<h2 align="left">📖 How It Works </h2>

The bot reads user messages that start with a designated character, such as '!', followed by the path to the file containing the API key, and the question separated by a delimiter, such as a comma. 

Upon launch, the bot informs the users of its fresh status and its lack of memory of previous conversations. As users engage, the bot generates responses, which are then sent back to the Discord channel.

The bot also manages the token count in the conversation to prevent exceeding the AI model's token limit. If the token count approaches the limit, the bot removes older conversations to free up tokens.


<h2 align="left">🚀 Usage </h2>

1. **Obtain Your API Key:** You will need an API key to use the AI model. This key should be saved to a local text file for future use.

2. **Get Your Discord Bot Token:** This requires creating a new application in the Discord developer portal, adding a bot to the application, and retrieving the bot's token. Detailed instructions can be found in the [Discord Developer Portal](https://discord.com/developers/docs/intro).

3. **Set Up Environment Variable:** To use the bot, you need to set the environment variable for your Discord Bot token. This allows the bot to authenticate with the Discord API. The process for setting this environment variable can vary based on your operating system.

4. **Running the Bot:** The bot can be started via the command line. Navigate to the directory containing the main file of the bot and run the bot using the relevant command.

5. **Interacting with the Bot:** Users interact with the bot by providing the API key file path and their question or message, separated by a delimiter.

**DETAILED USAGE IS FOUND IN VERSION FOLDER README**


<h2 align="left">🔜 Upcoming Features </h2>

There are plans to continually enhance the bot's capabilities and features, such as command execution and user control. Stay tuned for updates!


<h2 align="left">👨‍💻 Author </h2>

<div align="center">

 
  🔧 **Logan Falkenberg** - *Lead Developer*
  
  For any queries, discussions, or feedback, I am always open. Feel free to reach out:
  
  📧 **Email:** [loganf0101@gmail.com](mailto:loganf0101@gmail.com) 
  
  🌐 **GitHub:** [@TheTallProgrammer](https://github.com/TheTallProgrammer)
  
</div>


<h2 align="left">📜 License </h2>

<div align="center">
  
  This project is licensed under the terms of the Apache License 2.0. Please see [LICENSE](LICENSE./) for more details.
  
  ![License Logo](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
  
</div>
