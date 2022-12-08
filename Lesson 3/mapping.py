"""
Функция map() - значительное упрощение работы со списками и не только
"""

# Например, есть функция, принимающая в качестве аргументов некую функцию и некий список,
# а возвращать готовый список после "некой" функции
# (В названиях функций Камянецкий использовал язык запросов SQL)
def select(f, col):
    return [f(x) for x in col]

# И есть функция, принимающая в качестве аргументов опять-таки некую функцию и некий список,
# возвращающая обратно список после проверки условия выполнения "некой" функции:
def where(f, col):
    return [x for x in col if f(x)] # н-р, если f(x) - проверка на четность x

# Теперь мы можем формировать списки, передавая в написанные функции разные аргументы,
# в т.ч. лямбды и встроенные в Python функции
list1 = select(int, input().split())    # split для разделения, н-р, введенных через пробел чисел
print(list1)

list2 = where(lambda x: not x%2, list1)
print(list2)

even_list = select(lambda x: x**2, list2)
print(even_list)    # В итоге выведется список четных чисел, возведенных в квадрат

# *******************************
# MAPPING
# *******************************
# Всю вышеописанную логику выполняет в Python функция map()
# Важное примечание: если требуется вывод результатов работы map, нужна прямая типизация, т.е.
# приведение к типу "список", обернув map() в list(map())
list3 = list(map(int, '1, 2, 3, 4, 21, 74, 137'.split(',')))
print(list3)   # [1, 2, 3, 4, 21, 74, 137]

list4 = list(map(lambda x: x**2, list3))
print(list4)   # [1, 4, 9, 16, 441, 5476, 18769]

# Формирование списка из текстового файла с четными числами, возведенными в квадрат
# в виде кортежей "(число, квадрат числа)" c использованием маппинга
path = 'Lesson 3\data.txt'
with open(path, 'r') as file:
    even = [(i, i**2) for i in map(int, file.read().split()) if not i%2]
print(even)

# У map() есть еще одна особенность: это однократный итератор, т.е. обратиться повторно
# к результату его работы не получится, это видно из примера ниже:

data = map(int, '1, 2, 3'.split(','))

for e in data:
    print(e, end=' ') # 1 2 3

# Попробуем запустить повторно
print('******')

for e in data:
    print(e, end=' ') # Ничего не выведется
# Чтобы такого не было, необходимо результат маппинга принудительно сохранить в виде списка,
# обернув map() в list(map()):
data = list(map(int, '1, 2, 3'.split(',')))