import math

# Домашняя работа к семинару 1

"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""

day_num = int(input('Введите число, обозначающее день недели: '))
while 1 > day_num or day_num > 7:
    day_num = int(input('Число должно быть от 1 до 7! Введите заново: '))

if day_num > 5:
    print('День выходной')
else: print('День рабочий')


"""
Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
print('x', 'y', 'z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            statement = not (x and y and z) == (not x or not y or not z)
            print(x, y, z, '\t', statement)


"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

def user_input(x_or_y):
    x_or_y = int(input(f'Введите значение {x_or_y}, отличное от 0: '))
    while x_or_y == 0:
        x_or_y = int(input(f'Число должно быть отличным от 0! Введите еще раз: '))
    print()
    return x_or_y


def what_quarter(x, y):
    quarter = 1
    if x < 0:
        if y < 0: quarter = 3
        else: quarter = 2
    elif y < 0: quarter =4
    return quarter


x = user_input('x')
y = user_input('y')
quarter = what_quarter(x, y)
if quarter == 2:
    print(f'Точка {x, y} лежит во 2-й плоскости')
else:
    print(f'Точка {x, y} лежит в {quarter}-й плоскости')

"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y)
"""
quarter_ranges = {1: 'x = от 1 до ∞ \ny = от 1 до ∞',
                  2: 'x = от -1 до -∞ \ny = от 1 до ∞',
                  3: 'x = от -1 до -∞ \ny = от -1 до -∞',
                  4: 'x = от 1 до ∞ \ny = от -1 до -∞'
                  }


def user_input():
    i = int(input('Введите номер четверти: '))
    while i > 4 or i < 1:
        i = int(input(f'Число должно быть в диапазоне от 1 до 4! Введите еще раз: '))
    print()
    return i


quarter_num = user_input()
print(f'Диапазон возможных координат точек в этой четверти: \n'
      f'{quarter_ranges[quarter_num]}')

"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""

def user_input(x_or_y):
    x_or_y = int(input(f'Введите значение {x_or_y}: '))
    return x_or_y


def find_distance(x1, y1, x2, y2):
    print(f'Заданы две точки с координатами ({x1}, {y1}) и ({x2}, {y2}).\n'
          f'Расстояние между точками {((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5}')
    # print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


print("Задайте последовательно координаты двух точек.")
x1 = user_input('x1')
y1 = user_input('y1')
x2 = user_input('x2')
y2 = user_input('y2')

print()
find_distance(x1, y1, x2, y2)
