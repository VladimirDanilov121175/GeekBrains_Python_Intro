import write
import view
import edit


def bot_start():
    print('♦' * 3)
    user_input = input('Какую операцию хотите выполнить?\n'
                       '1 - Новая запись\n'
                       '2 - Чтение\n'
                       '3 - Редактирование существующей записи\n'
                       'exit - завершить работу\n'
                       '>>> ')

    if user_input == '1':
        write.new_entry()
    elif user_input == '2':
        view.storage_items()
    elif user_input == '3':
        edit.change_entry()
    elif user_input == 'exit':
        print('Работа завершена')
    else:
        print('Ошибка ввода!')
        bot_start()

