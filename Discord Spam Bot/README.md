### Prerequisites:

1.  Install Python: Make sure you have Python installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2.  Install Discord.py: Open a terminal or command prompt and run the following command to install the Discord.py library:

    `pip install discord.py`

### Bot Setup:

1.  Get Your Discord Bot Token:

    -   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    -   Create a new application.
    -   Go to the "Bot" tab and click "Add Bot."
    -   Copy the bot token from the "TOKEN" section.
2.  Enable Privileged Intents:

    -   In the Discord Developer Portal, navigate to the "Bot" tab.
    -   Under the "Privileged Gateway Intents" section, enable the "Message Content" intent.

### Modify the Python Script:

1.  Replace Token and Channel ID:
    -   Open the Python script (the `.py` file) in a text editor.
    -   Replace `'YOUR_DISCORD_BOT_TOKEN'` with the bot token you copied.
    -   Set the `channel_id` variable to the ID of the channel where you want the messages to be sent.

### Run the Bot:

1.  Run the Script:
    -   Save the changes to the Python script.

    -   Open a terminal or command prompt.

    -   Navigate to the directory containing your Python script.

    -   Run the script:

        `python your_script_name.py`

        Replace `your_script_name.py` with the actual name of your Python script.

### Invite the Bot to Your Server:

1.  Generate an Invite Link:
    -   Go to the Discord Developer Portal.
    -   Select your application (bot) from the list.
    -   Go to the "OAuth2" tab.
    -   Under "OAuth2 URL Generator," select the "bot" scope and the required bot permissions.
    -   Copy the generated URL and paste it into your browser to invite the bot to your server.

### Verify and Test:

1.  Verify Bot Status:

    -   Check the terminal where the script is running. You should see a message indicating that the bot has logged in.
2.  Test the Bot:

    -   Go to the Discord server where you invited the bot.
    -   Wait for the scheduled messages to be sent based on the specified time interval.

This was generated with chat gpt 3.5. I'm lazy.
