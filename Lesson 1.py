# print('Введите что-нибудь: ')
# a = input()
# print('Введите еще что-нибудь')
# b = input()

# # Разные способы вывода
# print(a, b)     # Выведется без запятой
# print('{}, {}'.format(a, b))
# print('{1}, {0}'.format(a, b))  # сперва выведется b
# print(f'{a}, {b}')

# ****************************************************************
# Особенности некоторых арифметических операций
# ****************************************************************

# print(11 / 3)    # выведется вещественное число 3.6666666666666665
# print(11 // 3)    # выведется целое число 3, т.е. без остатка
# print(11 % 3)    # выведется остаток деления, т.е. 2
# print(3 * 1.3)    # выведется странное число 3.9000000000000004 (связано с особенностями хранения вещественных чисел)
# # Поэтому...
# print(round(3 * 1.3, 1)) # Выводится 3.9, после запятой указывается количество символов после запятой
# print(round(23 / 3, 6))  # 7.666667  c 6 знаками после запятой

# ****************************************************************
# Управляющие конструкции
# ****************************************************************

# Инвертирование числа с использованием while
# original = int(input('Введите число: '))
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + original % 10
#     original //= 10
# print(inverted)

# # While - else. Else начинает работать, когда заканчивается тело цикла while
# original = int(input('Введите число: '))
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + original % 10
#     original //= 10
# else:
#     print('Цикл while закончен')
# print(inverted)

# # Управляющая конструкция for in range()
# for i in range(5):
#     print(i)        # Выведет числа от 0 до 4 (как в индексах)

# for i in range(1, 5):
#     print(i)        # Выведет числа от 1 до 4

# for i in range(1, 10, 2):
#     print(i)          # Выведет числа от 1 до 9 с шагом 2

# for i in 'qwe-rty':
#     print(i) # Побуквенно разберет слово и выведет в консоль

# ****************************************************************
# Работа со строками
# ****************************************************************
text = 'съешь еще этих мягких французских булочек'

# print(len(text))    # количество символов в строке (41)
# print('еще' in text) # True
# print(text.isdigit())   # False
# print(text.islower())   # True
# print(text.replace('еще', 'ЕЩЕ')) # Заменит фрагмент на новый

# Срезы строк

# print(text[0]) # 'c'
# print(text[len(text)-1]) # 'к'
# print(text[0:]) # whole text
# print(text[:len(text)]) # whole text
# print(text[0:len(text)]) # whole text
# print(text[:]) # whole text
# print(text[len(text) - 4:])  # очек
# print(text[-10:])   # их булочек (10 c конца и до конца)
# print(text[0:len(text):6])  # сеикакл (от начала до конца с шагом 6)
# print(text[::6])  # сеикакл (от начала до конца с шагом 6)
# print (text[::-1])  # Выведет всю строку наоборот )))

# text = text[-10] + text[:2] + text[15:len(text)-15]
# print(text)

# ****************************************************************
# Работа со списками
# ****************************************************************
# ran = range(1, 5)
# numbers = list(ran)
# print(type(numbers), type(ran))
# print(numbers)
# # Далее - наглядная демонстрация, что перезапись переменной в списке не переписывает список
# for i in numbers:
#     i *= 2
#     print(i)    # 2, 4, 6, 8
# print(numbers)  # 1, 2, 3, 4

colors = ['red', 'green', 'blue']
for c in colors:
    print(c)    # red, green, blue
for c in colors:
    print(c*2) # redred, greengreen, blueblue

colors.append('gray') # добавится новый цвет в конец списка
print(colors == ['red', 'green', 'blue', 'gray'])   # True

colors.remove('green')  # удалит цвет
# или другой способ с явным указанием на удаление:
del colors[0]
print(colors)


