
# GPT-Oracle Ultra 🌐

Welcome to the **GPT-Oracle Ultra Chatbot** v1.5.0, an advanced language model bot tailored for Discord. Based on OpenAI's latest GPT-3.5 Turbo technology, this bot redefines interactive experiences with its intuitive conversational capabilities. Designed for large server environments and multi-server setups, it ensures optimal performance and delivers personalized responses with its user-specific API key storage mechanism.

---

## 🆕 What's New in v1.5.0

This updated version of GPT-Oracle Ultra introduces several enhancements, making your interactions with the bot more efficient, reliable, and fun.

- 🎨 **Integration of DALLE 2 AI Art Generator**: OpenAI's DALLE 2 AI art generator is now part of the bot, enabling users to generate unique images based on their prompts via the `!draw` command.

- 🗃️ **Database Functions for API Keys**: We've transitioned from direct file I/O to database functions (`get_api_key` and `save_api_key`) for managing API keys. This change promotes efficiency and improves performance.

- ✅ **API Key Validation**: The bot now validates your API key before saving it with the `validate_api_key` function. This ensures the validity of the provided OpenAI API key before use.

- 🛠️ **Improved Error Handling**: We've added detailed try-except blocks around the `ask` and `draw` commands to handle more types of errors.

- 💬 **Typing Indicator**: To make the bot seem more interactive and human-like, a typing indicator is shown when the bot is responding.

- 🚀 **In-Memory Storage for API Keys**: For improved performance, the bot now stores API keys in memory after their first use, reducing the need for database operations.

---

## 🛡️ Security First

The security of your data has always been our top priority. We've taken several measures to ensure that your API keys are safe and accessible only when needed. 

### 🔑 Secure API Key Storage

Users' API keys are securely stored in a SQL database, retrieved only when necessary for user interaction. Please note that the user's responsible for creating their own database for use with this bot. I've shared the detailed instructions on setting up and integrating the database below.

### 🚦 Command Access Control

Every `!ask` command triggers a search for the user's API key associated with their ID. No key, no access — this ensures only authorized users can engage with the bot. 

### 🕵️ Private Key Saving

The `!save_key` command is the gateway to storing your API key, executable solely via direct messages with the bot to prevent exposure in public or group chats. 

---

## 🌟 Features 

- 🧠 AI Chatbot: Harness the prowess of gpt-3.5-turbo-16k, a groundbreaking language model, for responsive, dynamic interactions.
- 🎨 AI Art Generator: Leverage the creativity of DALLE 2, an AI art generator, to create unique images from your prompts.
- 🔨 Customizability: Tailor the bot's actions to your liking by tweaking the system message in the conversation initialization.
- 🚀 Auto Responses: On startup, a message is sent, alerting users of a fresh instance and previous conversations being discarded.
- 📚 Intelligent Character Limit Handling: The bot skillfully tackles Discord's 2000 character limit per message, splitting and dispatching information across multiple messages if necessary.

## 📘 How It Works 

GPT-Oracle Ultra processes user commands and messages, responding accordingly. Three commands are essential to its functionality: `!save_key`, `!ask`, and `!draw`.

- `!save_key`: This command, followed by the API key, helps in storing the API key securely in a SQL database.
- `!ask`: A command followed by a question triggers GPT-4, providing detailed responses to your queries.
- `!draw`: This command, followed by a prompt, enables DALLE 2 creating unique images based on your input.

---

## 🚀 Getting Started 

Integration of your SQL database and Discord account involves a series of simple steps outlined below.

### Database Integration

**Please note that it is your responsibility to create and set up your own SQL database for use with this bot. The project is designed to allow you to easily implement your own database.**

1. **Database Structure Setup**

    A `UserData` table in your SQL database is required to store the user IDs and associated API keys. The SQL command for creating this table is:

    ```sql
    CREATE TABLE UserData (
        UserID BIGINT PRIMARY KEY,
        ApiKey VARCHAR(255) NOT NULL
    );
    ```

    Execute this command in your SQL database to set up the table correctly.

2. **Connect to the Database**

    You need to fill out the required details in the `connect_to_database` function in the `database.py` file.

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

    Replace `'host'`, `'user'`, `'password'`, `'db'`, and `'0000'` with your actual database details (host, user, password, database name, and port). Ensure these are enclosed in quotes ('').

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

To interact with the bot, use the `!ask` or `!draw` command followed by your query. This can be done in any channel where the bot is present. Here's an example:


    !ask What is the meaning of life?
    !draw Paint me a picture of a happy duck


After making any changes, remember to save and restart your bot for the updates to take effect.


## 👨‍💻 Author 

Logan Falkenberg - *Lead Developer*

For any queries, discussions, or feedback, please feel free to reach out:

📧 **Email:** [loganf0101@gmail.com](mailto:loganf0101@gmail.com) 

🌐 **GitHub:** [@TheTallProgrammer](https://github.com/TheTallProgrammer)

---

## 📜 License 

This project is licensed under the terms of the Apache License 2.0. For more details, please see [License](../LICENSE)
