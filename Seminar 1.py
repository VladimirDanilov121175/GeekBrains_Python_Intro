'''
1. Напишите программу, которая принимает на вход два числа и проверяет,
является ли одно число квадратом другого.
    *Примеры:*

    - 5, 25 -> да
    - 4, 16 -> да
    - 25, 5 -> да
    - 8,9 -> нет
'''

print('Введите первое число:')
a = int(input())
print('Введите второе число:')
b = int(input())

if b == a ** 2 or a == b ** 2:
    print('Да')
else:
    print('Нет')

'''
2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
        Примеры:
    - 1, 4, 8, 7, 5 -> 8
    - 78, 55, 36, 90, 2 -> 90
'''

list = [- 1, 4, 8, 19, 5]
max = list[0]

for i in list:
    if i > max:
        max = i
print(max)

# Второй вариант решения
max_num = None
print('Введите 5 чисел')
for i in range(5):
    a = int(input(f'Число {i+1}: '))
    if i == 0:
        max_num = a
    elif a > max_num:
        max_num = a
print(f'Максимальное число - {max_num}')


'''
1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
        *Примеры:*
        - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
'''

print('Введите число:')
a = int(input())

for i in range(-a, a + 1):
    print(i, end=', ')

"""
2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    *Примеры:*
    - 6,78 -> 7
    - 5 -> нет
    - 0,34 -> 3
"""
# Способ 1
num = float(input('Введите дробное число: '))
print(int(num * 10 % 10))

# Способ 2
while num > 10:
    num %= 10
print(str(num)[2])

# Способ 3
print(input('Введите дробное число: ').split(',')[1][0])

"""
Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
"""
num = int(input('Введите число: '))
if (num % 5 + num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print('Число соответствует условию')
else:
    print('Число не соответствует условию')
