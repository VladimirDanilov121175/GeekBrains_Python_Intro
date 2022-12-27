from operator import itemgetter
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from credits import bot_token

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
weekdays = {1: 'MN.txt', 2: 'TUE.txt', 3: 'WDN.txt', 4: 'THU.txt', 5: 'FR.txt', 6: "STD.txt", 7: 'SUN.txt'}


def get_day(update, context):
    keyboard = [
        [InlineKeyboardButton('Понедельник', callback_data='1')],
        [InlineKeyboardButton('Вторник', callback_data='2')],
        [InlineKeyboardButton('Среда', callback_data='3')],
        [InlineKeyboardButton('Четверг', callback_data='4')],
        [InlineKeyboardButton('Пятница', callback_data='5')],
        [InlineKeyboardButton('Суббота', callback_data='6')],
        [InlineKeyboardButton('Воскресенье', callback_data='7')]
    ]
    context.bot.send_message(update.effective_chat.id, 'Выбери день недели', reply_markup=InlineKeyboardMarkup(
        keyboard))


def start(update, context):
    sel = [
        [InlineKeyboardButton('Чтение', callback_data='8')],
        [InlineKeyboardButton('Добавление', callback_data='9')],
        [InlineKeyboardButton('Замена', callback_data='10')]
    ]
    context.bot.send_message(update.effective_chat.id, 'Выбери действие:', reply_markup=InlineKeyboardMarkup(sel))


def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '8':
        get_day(update, context)
        # context.bot.send_message(update.effective_chat.id, answer)
    elif query.data == '9':
        context.bot.send_message(update.effective_chat.id, 'Добавление')
    elif query.data == '10':
        context.bot.send_message(update.effective_chat.id, 'Замена')


button_handler = CallbackQueryHandler(button)
getday_handler = CallbackQueryHandler(get_day)
start_handler = CommandHandler('start', start)
# getday_handler = CommandHandler('getday', get_day)

dispatcher.add_handler(start_handler)
# dispatcher.add_handler(getday_handler)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()
