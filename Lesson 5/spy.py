import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('bot_log.csv', 'a', encoding='utf-8') as f:
        f.write(f'{datetime.datetime.now()}: '
                f'{update.effective_user.first_name}, '
                f'{update.effective_user.last_name}, '
                f'{update.effective_user.id}, '
                f'{update.message.text}\n')
