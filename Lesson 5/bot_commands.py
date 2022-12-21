from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import log


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/help\n/time\n/sum')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Время {datetime.datetime.now().strftime("%H:%M:%S")}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    items = msg.split()
    num1 = int(items[1])
    num2 = int(items[2])
    res = num1 + num2

    await update.message.reply_text(f'{num1} + {num2} = {res}')
