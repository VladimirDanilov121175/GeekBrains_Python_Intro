"""
В файле хранятся некие числа. Необходимо выбрать из этих чисел четны
и составить список пар по принципу "число, квадрат числа"
Пример:
1 2 3 15 38 54 38 17 133 29 78
Должны получить:
[(1, 1), (2, 4), (3, 9), (15, 225)...]
"""
# Открываем файл
init_list = []
path = 'Lesson 3\data.txt'

# Способ 1 - работает только, если числа в файле записаны в каждую строку отдельно
# with open(path, 'r') as file:
#     for num in file:
#         init_list.append(int(num))
# print(init_list)

# g = lambda x: x**2
# even_list = [(i, g(i)) for i in init_list if not i%2]
# print(even_list)


# Способ 2 - для варианта, если числа записаны в 1 строку через пробел
# Способ показан Сергеем Камянецким в лекции
with open(path, 'r') as f:
    data = f.read() + ' '   # дополнительный пробел в конце нужен для корректной работы ниже
print(data)

# while data != '':
#     pos = data.find(' ')
#     init_list.append(int(data[:pos]))
#     data = data[pos + 1:]

# Записанный выше алгоритм преобразования в список можно было записать одной строкой:
# init_list = data.split()
# # Но тогда необходимо:
# init_list = [int(i) for i in init_list]

print(init_list)

even_list = [(i, i**2) for i in init_list if not i%2]
print(even_list)
 