# Задача из видеокурса GB "Основы Python"

"""Компьютер загадывает случайное число от 1 до 100.
Пользователю предлагается его угадать.
Если пользователь угадал, программа сообщает о победе.
Если пользователь ввел неверно число, программа дает ему подсказку: введенное число больше или меньше загаданного."""

from random import randint

users = {}
for i in range(3):
    users[i] = input(f"Имя игрока № {i}: ")

winner = None
num_to_guess = randint(1, 100)
try_count = 0
tries_allowed = 0
user_try = None

difficulty = input('Выберите уровень сложности:\n'
                   '1 - сложный\n'
                   '2 - средний\n'
                   '3 - легкий\n>>>')
if difficulty == '1': tries_allowed = 5
if difficulty == '2': tries_allowed = 15
if difficulty == '3': tries_allowed = 25


print('Угадайте загаданное число от 1 до 100')

while user_try != num_to_guess and try_count != tries_allowed:
    for i in users:
        try_count += 1
        user_try = int(input(f'Играет {users[i]}. Попытка № {try_count} >>> '))
        if user_try < num_to_guess:
            print("Больше!")
        elif user_try > num_to_guess:
            print("Меньше!")
        else:
            print("БИНГО!!!!")
            winner = users[i]
            break

else:
    if try_count == tries_allowed:
        print('Попыток больше не осталось, никто не угадал')
    else:
        print(f'Угадал {winner} на {try_count} попытке.')
