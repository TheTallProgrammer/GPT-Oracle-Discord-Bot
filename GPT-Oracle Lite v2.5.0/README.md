# 🤖 GPT-Oracle Discord Bot Lite v2.5.0 🚀

The GPT-Oracle Discord Bot v2.5.0 introduces powerful and engaging new capabilities while retaining the user-friendly approach and functionality of previous versions. The bot continues to leverage state-of-the-art language models for interactive conversations and has expanded its horizons with innovative additions like the DALLE 2 AI art generator. This update also enhances user experience and convenience with features such as asynchronous file I/O and API key validation.

## 📌 What's New in v2.5.0

The v2.5.0 version comes with an array of enhancements that streamline the user interaction and introduce new opportunities for creativity and engagement:

-   **DALLE 2 AI Art Generator Integration**: The bot now offers the `!draw` command that uses the advanced capabilities of OpenAI's DALLE 2 AI art generator to create unique and impressive images based on user prompts.

-   **Asynchronous File I/O**: Instead of using traditional file operations, the bot now leverages the `aiofiles` module for asynchronous file I/O. This helps to prevent the bot from blocking while waiting for file operations, leading to improved performance and responsiveness.

-   **API Key Validation**: The bot now includes an API key validation function to check the validity of a provided OpenAI API key before using it.

-   **In-Memory API Key Storage**: For better performance, the bot now stores API keys in memory after the first use, reducing the need for file operations.

## 📋 Available Commands

The Discord bot offers the following commands to interact with its various functionalities:

-   **!save_key**: This command enables users to securely save their API key. Once saved, the key is used for all subsequent interactions without the need to provide the API key for each input.

-   **!ask**: The `!ask` command allows users to directly communicate with the GPT-3.5 Turbo model. By providing a prompt or question, users can receive intelligent and contextually relevant responses from the model.

-   **!draw**: The new addition in this version, the `!draw` command, allows users to tap into the immense creativity of the **DALLE 2** AI art generator. By supplying a prompt, users can generate unique and mesmerizing art pieces.

## ⚠️ Security

As in the previous versions, the Lite version stores the literal API key locally on the user's system. While this provides the benefit of simplicity and does not require a database, it's less secure than the Plus version. Be sure to secure your system and avoid sharing your API key or the file containing the key with others. Misuse of API keys can lead to unwanted requests or charges.

## 🗝️ Obtain Your OpenAI API Key

The operation of the GPT-Oracle bot integrates with OpenAI's GPT and DALLE models, necessitating an OpenAI API key. You can [create your OpenAI API key](https://platform.openai.com/account/api-keys) by registering a free account. Be sure to save your API key securely, as it's displayed only once during creation.

## 📖 Usage and Tips

The GPT-Oracle Discord Bot Lite Version is designed to be easy and straightforward to use. Interaction remains largely similar to previous versions, with the key addition of the `!save_key` command.

To set up the bot with your discord server:

1. Open the `main.py` file in the codebase.
2. Locate the following line towards the end of the file:

    ```python
    TOKEN = 'TOKEN'
    bot.run(TOKEN)
    ```

3. Replace `'TOKEN'` with your actual Discord bot token, making sure it is enclosed in quotes ('').

Now, your GPT-Oracle Plus Bot is ready to go!

To make usage even more seamless, you can store your API key locally using the `!save_key` command. Follow these steps to do so:

1. Open a Direct Message (DM) with the bot.

2. Type the command `!save_key` followed by your API key. For instance:

    ```
    !save_key abcdef123456
    ```

3. Press Enter to send the message. The bot will store your API key locally on your system, eliminating the need to enter it each time you want to interact with the bot.

Now, your API key is ready for all future interactions without needing to repeat the process. Please remember to handle your API key with care as it is sensitive information.

Please note that you need to replace `abcdef123456` with your actual API key. Always ensure that your API key is secure and not shared or exposed. For any further assistance, please reach out to the developer.

To interact with the bot, simply use the `!ask` or `!draw` command followed by your query. For example:

    !ask What is the meaning of life?
    !draw Paint me a picture of a scenic landscape

## 👨‍💻 Author

Logan Falkenberg - _Lead Developer_

For queries, assistance, or feedback, reach out:

📧 **Email:** [loganf0101@gmail.com](mailto:loganf0101@gmail.com)

🌐 **GitHub:** [@TheTallProgrammer](https://github.com/TheTallProgrammer)

---

## 📜 License

This project is licensed under the terms of the Apache License 2.0. For more details, please see [License](../LICENSE).
