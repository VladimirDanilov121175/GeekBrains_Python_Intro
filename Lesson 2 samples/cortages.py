# # Если необходимо сделать кортеж из 1 элемента, обязательно поставить запятую
# # Иначе программа воспримет это как обычное число
# t = (1,)
# print(t)   # (1,)
# print(type(t)) # tuple
#
# t = (1)
# print(t)   # 1
# print(type(t))  # int

# Распаковка кортежей с одновременным присвоением его значений отдельным переменным
t = ('red', 'green', 'blue')
red, green, blue = t
print(t)   # ('red', 'green', 'blue')
print('{}, {}, {}'.format(red, green, blue))   # red, green, blue

