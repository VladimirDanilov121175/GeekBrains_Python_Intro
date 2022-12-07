# Упрощенное формирование списков, в т.ч. двумерных

# Формирование простого списка
list1 = [x **2 for x in range(10)]
print (list1)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

list2 = [x**2 for x in range(10) if x%2 == 0]  # только для четных
print(list2)    # [0, 4, 16, 36, 64]

# Заполнение списка кортежами с результатами работы функций
def f(x):
    return x**3

list3 = [(i, f(i)) for i in range(1, 10) if not i%2]
print(list3)    # [(2, 8), (4, 64), (6, 216), (8, 512)]

# Через лямбду
cube = lambda x: x**3
list4 = [(i, cube(i)) for i in range(1, 10) if not i%2]
print(list4) # [(2, 8), (4, 64), (6, 216), (8, 512)]

# Двумерный список 5 на 5, заполненный нулями
list5 = [[0 for _ in range(5)] for _ in range(5)]
print(list5)
