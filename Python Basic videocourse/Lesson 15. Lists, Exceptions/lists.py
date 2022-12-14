import math
from random import randint
from math import sqrt

# # Решить с помощью генераторов списка.
# # 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# # Примечание: Списки фруктов создайте вручную в начале файла.
# fruits1 = 'яблоки, груши, бананы, апельсины, мандарины, киви, виноград'.split(', ')
# fruits2 = 'гранаты, манго, кокосы, апельсины, хурма, мандарины, фейхоа, авокадо'.split(', ')
#
# new_list = [i for i in fruits1 if i in fruits2]
# print(new_list)
# print(type(new_list))

# # 2: Дан список, заполненный произвольными числами. Получить список из элементов исходного,
# # удовлетворяющий следующим условиям:
# # Элемент кратен 3,
# # Элемент положительный,
# # Элемент не кратен 4.
# # Примечание: Список с целыми числами создайте вручную в начале файла.
# # Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
# nums = [randint(-100, 100) for _ in range(30)]
# print(nums)
# new = [num for num in nums if num > 0 and not num % 3 and num % 4]
# print(new)

# # 3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список
# # из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное)
# # и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# # В результате работы функции исходный список не должен измениться.
# # Например:
# # old_list = [1, -3, 4]
# # result = [1, -3, 2]
# # Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
# # 10-20 чисел в списке вполне достаточно.
#
# nums = [randint(-100, 100) for _ in range(10)]
# print(nums)
# new_list = [math.sqrt(num) if num > 0 else num for num in nums]
# print(new_list)

"""
4. Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число. Введенное число передаем параметром 
в написанную функцию и печатаем результат, который вернула функция. Обработать возможность возникновения 
исключительной ситуации, которая поднимается внутри функции.
"""


def square(num):
    if num == 13:
        raise ValueError("Ошибка. Введено число 13")
    else:
        return num ** 2


input_num = int(input('Enter a number: '))

try:
    res = square(input_num)
    print(res)
except ValueError as err:
    print(err)
