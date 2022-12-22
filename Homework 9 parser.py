from bs4 import BeautifulSoup as bs
import requests

recipe_titles = []
recipes_urls = []

for i in range(1, 13):
    url = f'https://wikigrib.ru/gribnaya-kulinariya/page/{i}/'
    html = requests.get(url).text

    soup = bs(html, 'html.parser')
    result = soup.find_all('a', class_="catcont-list__title")
    for line in result:
        recipe_titles.append(line.text)
        recipes_urls.append(line['href'])

cook_book = {recipe_titles[i]: recipes_urls[i] for i in range(len(recipes_urls))}

print('РЕЦЕПТЫ БЛЮД С ГРИБАМИ')
for items in cook_book:
    print('{}: {}'.format(items, cook_book[items]))
