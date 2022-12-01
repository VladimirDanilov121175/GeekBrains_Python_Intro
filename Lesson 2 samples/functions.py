# Можно написать функцию в отдельном файле (print.py) и вызывать ее в основном коде
import print as p

print(p.print_symbol('*!*'))
print(p.print_symbol('4'))

# В Python функция может принимать неопределенное число аргументов
def concatenatio(*params):
    res: str = ''   # можно явно задавать тип данных
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))     # asdw
print(concatenatio('a', '11', str(type(328.1))))   # a11<class 'float'>
print(concatenatio('a', 11))  # TypeError: can only concatenate str (not "int") to str

# Пример рекурсии для вычисления чисел Фибоначчи
def fibonacci(num):
    if num in [1, 2]:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)

list = []
for e in range(1, 10):
    list.append(fibonacci(e))
print(list)
