# Вариант игры "Угадай число", где компьютер угадывает твое число

from random import randint

low = 1
high = 100
num = None
answer = None
count = 0

while answer != '=':
    count += 1
    num = randint(low, high)
    answer = input(f'Загадано число {num}? >>> ')
    if answer == '>':
        low = num + 1
    elif answer == '<':
        high = num - 1
print(f"Компьютер угадал на {count} попытке")
