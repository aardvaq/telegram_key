Telegram Keylogger Setup Guide

Requirements

Before running the script, ensure you have the following installed on your system:

Python 3.x (Download Python)

Required Python packages:

pynput

python-telegram-bot

Installation Steps

1. Clone or Download the Repository

If you haven't already, download the script or clone the repository.

# Clone the repository
git clone https://github.com/your-repo/telegram-keylogger.git
cd telegram-keylogger

2. Install Required Python Packages

Run the following command to install dependencies:

pip install pynput python-telegram-bot

3. Configure the Script

Open keylogger.py in a text editor and update the following variables with your Telegram bot token and chat ID:

api_token = 'YOUR_TELEGRAM_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

How to Get a Telegram Bot Token:

Open Telegram and search for @BotFather.

Start a chat and use the command /newbot.

Follow the instructions and copy the bot token.

How to Get Your Telegram Chat ID:

Open Telegram and search for @userinfobot.

Start a chat and type /start.

The bot will respond with your user ID (use this as chat_id).

4. Run the Script

Navigate to the script directory and run:

python keylogger.py

If python is not recognized, try:

python3 keylogger.py

5. Verify It’s Working

Start typing on your keyboard.

After 100 characters, you should receive a message in your Telegram bot.

If you don’t receive messages, check for errors in the terminal.

Troubleshooting

1. "No such file or directory" Error

Ensure you are in the correct directory before running the script:

cd path/to/script
python keylogger.py

2. "Can't parse entities" Error

The script uses ParseMode.HTML to avoid Markdown issues.

Ensure special characters like <, >, and & are properly escaped in the message.

3. "RuntimeError: Event loop is closed"

Restart your computer and try running the script again.

Make sure you are not running multiple instances of the script.

4. Telegram Bot is Not Sending Messages

Check if your bot is not blocked in Telegram.

Ensure your bot has permissions to send messages.

6. Stop the Keylogger

To stop the keylogger, press CTRL + C in the terminal.

Disclaimer

This script is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain permission before running this script on any system.
