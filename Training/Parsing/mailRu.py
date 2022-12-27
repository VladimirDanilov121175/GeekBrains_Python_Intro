from bs4 import BeautifulSoup as bs
import requests

html = requests.get("https://m.mail.ru/").text

soup = bs(html, 'html.parser')
result = soup.find_all('span', class_='list__item__title')
# print(soup)
for item in result:
    print(item.text)
