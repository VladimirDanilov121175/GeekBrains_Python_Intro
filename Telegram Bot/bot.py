from credits import bot_token
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler, CallbackQueryHandler
from bot_commands import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    bot = ApplicationBuilder().token(bot_token).build()

    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('menu', main_menu))
    bot.add_handler(CommandHandler('info', about_me))
    bot.add_handler(CallbackQueryHandler(button))

    bot.add_handler(MessageHandler(filters.TEXT, message))

    bot.run_polling()


if __name__ == '__main__':
    main()
