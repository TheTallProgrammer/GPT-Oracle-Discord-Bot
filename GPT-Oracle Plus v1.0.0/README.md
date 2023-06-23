
# 🤖 GPT-Oracle Plus 🚀

The **GPT-Oracle Plus Chatbot** is a powerful language model bot for Discord that uses OpenAI's GPT-3.5-turbo-16k model to answer user queries. It offers seamless interaction with users, and its advanced features make it an excellent choice for larger servers or environments with multiple servers. The bot enables users to store their individual API keys, allowing for personalized and optimized usage across various servers. Each user interaction is unique to the user's saved API key, which means that the bot provides individualized and custom responses based on each user's prior interactions. 

---

## 🛡️ Security 

### `Secure API Key Storage`

Security has been a primary focus during the development of the GPT-3.5-turbo Discord Chatbot Plus. Users' API keys are securely stored in an SQL database and are retrieved only when needed for user interaction. 

### `Command Access Control`

When a user attempts to use the `!ask` command, the bot will search the database for an API key associated with the user's ID. If no key is found, the user will not be able to use the command, ensuring that only authorized users can interact with the bot. 

### `Private Key Saving`

To further increase security, the `!save_key` command, which is used to store a user's API key, can only be executed through direct messages with the bot. This prevents the exposure of sensitive information in public or group chats. 

With these measures in place, users can confidently interact with the bot, knowing their information is securely stored.

---


## 🌟 Features 

- 🗣️ AI Chatbot: Utilizes the power of GPT-3.5-turbo-16k, one of the most advanced language models, for real-time, dynamic conversations.
- 🎟️ Token Count Limitation: Ensures that the conversation stays within GPT-3.5's token limits, managing older conversations when the token limit is reached.
- 🛠️ Customization: Can be easily customized to perform a variety of tasks by changing the system message in the conversation initialization.
- 🔒 Improved Security: The API key used for OpenAI's GPT-3.5 is now stored securely in a database. 
- 🗝️ API Key Validation: Validates the OpenAI API key before processing the user input. If the key is not valid, it notifies the user.
- 🚀 Automatic Responses: Sends an automatic message every time it is started, informing users that it's a fresh instance and previous conversations have been forgotten.
- 📝 Intelligent Character Limit Handling: The bot smartly handles Discord's 2000 character limit per message. If a response exceeds this limit, the bot splits the message and sends the remaining text in subsequent messages, ensuring you never miss any information due to Discord's character constraints.
- 🗂️ Database Integration: GPT-Oracle Plus integrates with a SQL database to securely store user API keys, enabling seamless interaction with the bot without having to input the key each time.

## 📖 How It Works 

The bot reads user commands and messages, processes them, and then responds. There are two commands that the bot can process: `!save_key` and `!ask`. The `!save_key` command saves the user's OpenAI API key to the database. This is done securely, and the `!save_key` command must be used in a direct message (DM) to the bot to ensure privacy. The `!ask` command is the primary way users interact with the bot, sending a message or question which the bot then responds to.

For example:

- Save the OpenAI API key: `!save_key YOUR_OPENAI_API_KEY`
- Ask a question: `!ask What is the capital of France?`

## 🗝️ Obtain Your OpenAI API Key

GPT-Oracle integrates with OpenAI's GPT model, necessitating an OpenAI API key for its operation. You can [create your OpenAI API key](https://platform.openai.com/account/api-keys) by registering a free account. 

**Please be aware, the API key is displayed just once, so ensure you save your API key to a local text file for future usage.** If misplaced, a new one will need to be generated.


## 🛠️ Setup and Integration

Setting up the GPT-Oracle Plus Bot involves integrating it with your SQL database and your Discord account. This guide provides comprehensive instructions to assist you in this process.


### Database Integration

1. **Set up the Database Structure**

    Your SQL database should contain a table `UserData` to store the user IDs and associated API keys. The SQL command for creating this table is:

    ```sql
    CREATE TABLE UserData (
        UserID BIGINT PRIMARY KEY,
        ApiKey VARCHAR(255) NOT NULL
    );
    ```

    Execute this command in your SQL database to set up the table correctly.

2. **Connect to the Database**

    - Open the `database.py` file in the codebase.
    - Locate the `connect_to_database` function:

    ```python
    def connect_to_database():
        # Replace these details with your actual database details
        conn = pymysql.connect(
            host='host',
            user='user',
            password='password',
            db='db',
            port=0000
        )
        return conn
    ```

    - Replace `'host'`, `'user'`, `'password'`, `'db'`, and `'0000'` with your actual database details (host, user, password, database name, and port). Ensure these are enclosed in quotes ('').

### Discord Integration

1. Open the `main.py` file in the codebase.
2. Locate the following line towards the end of the file:

    ```python
    TOKEN = 'TOKEN'
    bot.run(TOKEN)
    ```

3. Replace `'TOKEN'` with your actual Discord bot token, making sure it is enclosed in quotes ('').

2. To store your API key, you need to send a Direct Message (DM) to the bot on Discord. Type the command `!save_key` followed by your API key. For instance:

    ```
    !save_key abcdef123456
    ```

   Make sure to replace `abcdef123456` with your actual OpenAI API key. Note: the `!save_key` command should only be used in a DM with the bot to ensure the privacy of your API key.

To interact with the bot, use the `!ask` command followed by your query. This can be done in any channel where the bot is present. Here's an example:


    !ask What is the meaning of life?


After making any changes, remember to save and restart your bot for the updates to take effect.


## 👨‍💻 Author 

Logan Falkenberg - *Lead Developer*

For any queries, discussions, or feedback, please feel free to reach out:

📧 **Email:** [loganf0101@gmail.com](mailto:loganf0101@gmail.com) 

🌐 **GitHub:** [@TheTallProgrammer](https://github.com/TheTallProgrammer)

---

## 📜 License 

This project is licensed under the terms of the Apache License 2.0. For more details, please see [License](../LICENSE)


