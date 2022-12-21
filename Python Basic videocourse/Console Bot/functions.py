from datetime import datetime
import os
import shutil


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folders(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка под таким именем уже существует!')


def delete_file_or_folder(name):
    if os.path.exists(name):
        if os.path.isdir(name):
            os.rmdir(name)
        if os.path.isfile(name):
            os.remove(name)
    else:
        print(f'Не удается найти "{name}". Убедитесь, что такой файл или папка существуют')


def list_content(choice):
    li = os.listdir()

    if choice == 'folders':
        filtered_info = [f for f in li if os.path.isdir(f)]
        print(filtered_info)

    elif choice == 'files':
        filtered_info = [f for f in li if os.path.isfile(f)]
        print(filtered_info)

    elif choice is None:
        print(li)

    else:
        print(
            'Неправильный аргумент!\n'
            'list .......... показать все содержимое текущей папки\n'
            'list folders .. показать только папки\n'
            'list files .... показать только файлы'
        )


def write_info(name, info=None):
    with open(name, 'a', encoding='utf-8') as f:
        f.write('{}: {}\n'.format(datetime.now().strftime('%H:%M:%S'), info))


def show_info(name):
    with open(name, 'r', encoding='utf-8') as f:
        info = f.read()
        print(info)


def copy_file_or_folder(name, new_name):
    if not os.path.exists(name):
        print(f'Не удается найти "{name}". Убедитесь, что такой файл или папка существуют')
    elif os.path.exists(new_name):
        print(f'Файл или папка с таким именем {new_name} уже существуют!')
    else:
        if os.path.isfile(name):
            shutil.copy(name, new_name)
        if os.path.isdir(name):
            shutil.copytree(name, new_name)


def help_info():
    with open('help.txt', 'r', encoding='utf-8') as f:
        print(f.read())
