import interface


def output_entry(line):
    print('♦' * 3)
    li = line.split(';')
    for el in li[:-1]:
        print(el)


def storage_items():
    print('♦' * 3)
    with open("storage.txt", "r", encoding="utf-8") as file:
        data = file.read()
        query = input("Выберите опцию:\n"
                      "1 - Вывести информацию по всем артикулам\n"
                      "2 - Поиск информации по конкретному артикулу\n"
                      ">>> ")

        if query == "1":
            for line in data.split('\n'):
                output_entry(line)
        elif query == "2":
            search = input('Введите артикул целиком или первые несколько букв наименования >>> ')
            for line in data.split('\n'):
                if search in line:
                    output_entry(line)
                    break
        elif query not in data:
            print("Ничего не нашлось (((. Попробуйте изменить поиск.")

    print('♦' * 3)

    next_query = input('Искать еще? 1 - да / 2 - нет >>> ')
    if next_query == "1":
        storage_items()
    else:
        interface.bot_start()
