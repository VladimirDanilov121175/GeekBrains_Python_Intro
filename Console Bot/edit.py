import view
import interface


def change_entry():
    print('♦' * 3)

    # Converting found entry back to dict
    dict_to_change = {}
    old_entry = ''

    with open('storage.txt', 'r', encoding='utf-8') as file:
        old_data = file.read()

    user_input = input('Запись какого артикула хотите изменить?\n'
                       'Введите артикул целиком или первые несколько букв >>> ')
    if user_input not in old_data:
        print("Ничего не нашлось (((. Попробуйте изменить поиск.")
        next_query = input('Искать еще? 1 - да / 2 - нет >>> ')
        change_entry() if next_query == '1' else interface.bot_start()
    else:
        for lines in old_data.split('\n'):
            if user_input in lines:
                view.output_entry(lines)
                old_entry = lines
                break

        li = old_entry[:-1].split(';')  # Found entry converted to list
        for string in li:
            dict_key = string.split(': ')[0]
            dict_to_change[dict_key] = string.split(': ')[1]

        print('♦' * 3)

        # Changing values
        print('Введите новые значение или нажмите Enter для подтверждения прежних.')
        for key in dict_to_change:
            if key != 'Наименование артикула':
                value = input(f'{key}: ')
                if value != '':
                    dict_to_change[key] = value
        new_entry = ''
        for entries in dict_to_change:
            new_entry += '{}: {};'.format(entries, dict_to_change[entries])

        print('♦' * 3)

        # Updating storage.txt with modified entry
        new_data = old_data.replace(old_entry, new_entry)

        with open('storage.txt', 'w', encoding='utf') as file:
            file.write(new_data)

        next_query = input("Запись успешно изменена!"
                           "Редактировать другую запись? 1 - да, 2 - нет >>> ")
        change_entry() if next_query == '1' else interface.bot_start()
