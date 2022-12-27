from telegram import Update
from telegram.ext import ContextTypes
import requests
from bs4 import BeautifulSoup as bs


async def aphorism_day(update: Update, context: ContextTypes.DEFAULT_TYPE):
    html = requests.get('https://wisdomlib.ru/catalog/aforizmy').text

    soup = bs(html, 'html.parser')
    result = soup.find('div', {'class': 'story-day'}).find('div', {'class': 'content'}).find('p').text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)
