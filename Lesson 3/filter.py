"""
Встроенная функция filter() для фильтрации элементов списка по условиям некоей функции,
которую она принимает в качестве аргумента. Вторым аргументом выступает список
Как и map() является однократным итератором и требует прямого приведения к типу list()
для сохранения результата, если требуется неоднократное обращение к этому результату
"""
data = list(map(int, '1 2 3 4 87 99 132'.split()))
print(data) # [1, 2, 3, 4, 87, 99, 132]

data = list(filter(lambda x: not x%2, data))
print(data)   # [2, 4, 132]

# сложная однострочная запись
data = [(i, i**2) for i in list(filter(lambda i: not i%2, map(int, '1 2 3 4 87 99 132'.split())))]
print(data)  # [(2, 4), (4, 16), (132, 17424)]
