from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("5933564655:AAFztH1QvgGhVX5MEcmBeuCL8l3SIyd9o1w").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server started')

app.run_polling()