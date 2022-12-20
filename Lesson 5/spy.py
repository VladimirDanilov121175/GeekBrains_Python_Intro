import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import *


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('bot_log.csv', 'a') as f:
        f.write(f'{datetime.datetime.now()}: '
                f'{update.effective_user.first_name}, '
                f'{update.effective_user.id}, '
                f'{update.message.text}')
