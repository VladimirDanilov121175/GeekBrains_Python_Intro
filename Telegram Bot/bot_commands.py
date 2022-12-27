from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from weather import show_weather
from aphorism import aphorism_day
from currency import currency_rate


async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id,
        f"Данный бот был создан Даниловым Владимиром.\n"
        f"Связаться с автором: @danilov1975"
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    if user_input.lower() in ['инфо', 'info']:
        await about_me(update, context)
    else:
        await context.bot.send_message(update.effective_chat.id,
                                       text='Команда не распознана. Введите /start для показа главного меню')


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Прогноз погоды", callback_data='weather'),
         InlineKeyboardButton("Курсы валют", callback_data='currency'),
         InlineKeyboardButton("Игры", callback_data='games')],
        [InlineKeyboardButton("Афоризм дня", callback_data='aphorism'),
         InlineKeyboardButton("Об авторе", callback_data='about'),
         InlineKeyboardButton("Помощь", callback_data='help'),
         ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Главное меню'.upper(), reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        await about_me(update, context)
    elif query.data == 'weather':
        await show_weather(update, context)
    elif query.data == 'currency':
        await currency_rate(update, context)
    elif query.data == 'games':
        await context.bot.send_message(update.effective_chat.id, 'В разработке')
    elif query.data == 'help':
        await context.bot.send_message(update.effective_chat.id, 'В разработке')
    elif query.data == 'aphorism':
        await aphorism_day(update, context)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {update.effective_user.first_name}!"
    )
    await main_menu(update, context)
