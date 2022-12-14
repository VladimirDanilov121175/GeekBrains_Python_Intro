import interface


def new_entry():
    with open("storage.txt", 'a', encoding='utf-8') as file:
        entry = {
            "Наименование артикула": input('Наименование артикула: '),
            "№ ангара": input('№ ангара: '),
            "Ряд": input('Ряд: '),
            "№ стеллажа": input('№ стеллажа: '),
            "Наличие шт.": input('Наличие шт.: '),
        }
        for key in entry:
            file.write('{}: {};'.format(key, entry[key]))
        file.write('\n')

    print('♦' * 3)

    if input('Еще одну запись?\n1-да / 2-нет >>> ') == '1':
        new_entry()
    else:
        interface.bot_start()
