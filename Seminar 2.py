"""
1) Решить следующую задачу: генерируем среднее арифметическое последовательности дробных чисел, вводимых с клавиатуры.
После того как введем последнее число - программа выводит среднее арифметическое, максимальное и минимальное значение.
(не пользуемся списками и встроенными функциями)
Количество чисел задаётся в начале работы программы
"""

mean = 0
sum = 0
min = float('inf')
max = float('-inf')

for i in range(4):
    a = float(input('Введите число: '))

    sum = sum + a
    if a < min: min = a
    if a > max: max = a
mean = sum / 4
print(mean)
print(min)
print(max)


"""
2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.
"""
num = int(input('Введите число: '))

for i in range (1, 11):
    print(f'{num} * {i} = {num * i}')


"""
3) Решить следующую задачу, проверки знания таблицы умножения. Программа выводит 10 примеров
и выставляет за 10 правильных ответов - пять, за 9 и 8 - 4 балла, за меньше - три.
Если пользователь ошибся в каком-то ответе - сообщаем ему об этом
В итоге выводим количество верных ответов и оценку
"""
from random import randint
count = 0

for i in range(10):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    answer = int(input(f'{num1} * {num2} = '))
    if answer == num1 * num2:
        count += 1

if count == 10: print('Садись, пять!')
elif 7 < count < 10: print('Оценка 4')
else: print('Три')

"""
4) Решить следующую задачу,, выводящие на экран "электронный таймер".
Ставим таймер - часы, минуты, секунды.
После отсчета срабатывает будильник
"""
import time
import click
import pyglet

event = input('Задайте напоминание: \n')
print()

print('Задайте время, через которое должно сработать напоминание!')
hours = int(input('Часов: '))
minutes = int(input('Минут: '))
seconds = int(input('Секунд: ')) + minutes * 60 + hours * 3600
click.clear()

for value in range(seconds, 0, -1):
    hour = value // 3600
    minute = (value % 3600) // 60
    second = value - hour * 3600 - minute * 60
    print("Таймер запущен!\n")
    print('{}:{}:{}'.format(hour, minute, second))
    time.sleep(1)
    click.clear()
else: print(event)

# Вариант 2 от Михаила Лихачева
print('It`s timer.')
timer = input('Write time as format: HH:MM:SS \n')
time_str = timer.split(':')
all_times = []
for i in time_str:
    all_times.append(int(i))
song = pyglet.media.load('C:/Users/Mi/Desktop/Completed.mp3')

for i in range(all_times[0], -1, -1):
    for j in range(all_times[1], -1, -1):
        for l in range(all_times[2], -1, -1):
            if (i == 0 and j == 0) and l == 0:
                song.play()
                pyglet.app.run()
            else:
                print(f'{i}:{j}:{l}')
                time.sleep(1)
            all_times[2] -= 1
        all_times[1] -= 1
        all_times[2] += 60
    all_times[0] -= 1
    all_times[1] += 60

"""
5) Решить следующую задачу, которая вычисляет наибольший общий делитель двух целых чисел
"""

def find_gcd(x, y):
    if y > x:
        x, y = y, x

    while y != 0:
        x %= y
        x, y = y, x
    return x


num1 = int(input("Enter the first nuber: "))
num2 = int(input("Enter the second nuber: "))
gcd = find_gcd(num1, num2)

print('The GCD for {} and {} is {}'.format(num1, num2, gcd))
