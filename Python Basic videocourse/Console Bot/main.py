from functions import create_folders, delete_file_or_folder, write_info, copy_file_or_folder, \
    list_content, help_info, show_info, create_file
import sys

try:
    command = sys.argv[1]
except IndexError:
    print(
        'Необходимо ввести команду.\n'
        'Для вывода доступных команд введите "help"'
    )
else:
    if command == 'create_file':
        try:
            file_name = sys.argv[2]
            create_file(file_name)
        except IndexError:
            print('Отсутствует аргумент!')

    if command == 'create_folder':
        try:
            file_name = sys.argv[2]
            create_folders(file_name)
        except IndexError:
            print('Отсутствует аргумент!')

    if command == 'delete':
        try:
            name = sys.argv[2]
            delete_file_or_folder(name)
        except IndexError:
            print('Отсутствует аргумент!')

    if command == 'list':
        try:
            option = sys.argv[2]
        except IndexError:
            option = None
        list_content(option)

    if command == 'write':
        try:
            file_name = sys.argv[2]
            string = ' '.join(sys.argv[3:])
            write_info(file_name, string)
        except IndexError:
            print('Недостаточно аргументов!')

    if command == 'show':
        try:
            file_name = sys.argv[2]
            show_info(file_name)
        except IndexError:
            print('Отсутствует аргумент!')

    if command == 'help':
        help_info()

    if command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
            copy_file_or_folder(name, new_name)
        except IndexError:
            print('Недостаточно аргументов!')
