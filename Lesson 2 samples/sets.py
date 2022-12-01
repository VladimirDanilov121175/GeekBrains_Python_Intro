# # Множества
# colors_set = {'red', 'green', 'blue'}
# print(type(colors_set))  # <class 'set'>

# # Нельзя задать пустое множество через {}, необходимо прямое указание set()
# a = {}
# print(type(a))  # <class 'dict'>
#
# a = set()
# print(type(a))  # <class 'set'>

# # Базовые операции над множествами - добавление, удаление элементов
# colors_set.add('gray')
# print(colors_set)   # {'gray', 'blue', 'red', 'green'}
#
# # Повторное добавление gray ничего не даст, т.к. множество содержит только уникальные элементы
# colors_set.add('gray')
# print(colors_set)   # {'blue', 'red', 'gray', 'green'}
#
# colors_set.remove('red')
# print(colors_set)   # {'blue', 'green', 'gray'}
#
# # Повторное удаление red через remove() выдаст ошибку
# # colors_set.remove('red')
# # print(colors_set)   # KeyError: 'red'
#
# # Поэтому для удаления лучше использовать discard(), который не выдает ошибку, если удаляемого элемента нет
# colors_set.discard('red')
# print(colors_set)   # {'blue', 'green', 'gray'}
#
# # Очистка множества
# colors_set.clear()
# print(colors_set)   # set()

# Логические операции над множествами
a = {1, 2, 5, 3, 8, 6}
b = {5, 21, 7, 3, 9, 8}

c = a.copy()   # Создание копии множества
u = a.union(b)
print(u)    # {1, 2, 3, 5, 6, 7, 8, 9, 21}
i = a.intersection(b)
print(i)    # {8, 3, 5}
d1 = b.difference(a)
print(d1)   # {9, 21, 7}
d2 = a.difference(b)
print(d2)   # {1, 2, 6}

q = a.union(b).difference(b.intersection(a))
print(q)    # {1, 2, 6, 7, 9, 21}

# Замороженные (неизменяемые множества)
s = frozenset(a)
s.add(44)
print(s)    # AttributeError: 'frozenset' object has no attribute 'add'
