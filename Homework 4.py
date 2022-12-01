from random import randint

# 1) Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

rand_list = []
length = int(input("Задайте длину списка: "))
result = 0

for i in range(length):
    rand_list.append(randint(0, 100))
    if i % 2 == 1:
        result += rand_list[i]
print(f'Дан список чисел {rand_list}\n'
      f'Сумма всех чисел на нечетных позициях = {result}')


# 2) Написать программу, которая генерирует двумерный массив на A x B элементов (A и B вводим с клавиатуры)
# и считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

a = int(input('a = '))
b = int(input('b = '))
ab_list = []

for index in range(a):
    ab_list.append([])
    for value in range(b):
        ab_list[index].append(randint(1, 10))

print(f'Сгенерирован двумерный список: {ab_list}')
print('Среднее арифметическое по строкам: ')

for i in range(a):
    b_sum = 0
    for j in range(b):
        b_sum += ab_list[i][j]
    print(f'Индекс {i} - {b_sum / b}')


# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

rand_list = []
for _ in range(30):
    rand_list.append(randint(0, 100))

min_i = 0
for i in range(0, 29):
    for j in range(i + 1, 30):
        if rand_list[j] < rand_list[min_i]:
            min_i = j
    rand_list[i], rand_list[min_i] = rand_list[min_i], rand_list[i]

print(f'Сортированный список чисел {rand_list}')
