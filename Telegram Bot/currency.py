from telegram import Update
from telegram.ext import ContextTypes
import requests
from pprint import pprint
from bot_commands import *


async def currency_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    json = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    pprint(json)

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Текущий курс валют ЦБ РФ:\n')
    for key, value in json['Valute'].items():
        if key in ['USD', 'EUR', 'CHF', 'GBP', 'JPY']:
            string = '{} {} ({}) = {} рублей (RUB)'.format(
                value['Nominal'], value['Name'], value['CharCode'], value['Value']
            )
            await context.bot.send_message(chat_id=update.effective_chat.id, text=string)
