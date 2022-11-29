# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатеричную систему счисления.
input_num = int(input("Enter a number: "))
hex_convert = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

division = None
hex_digit = ''

while input_num != 0:
    division = input_num // 16

    if input_num % 16 > 9:
        hex_digit = hex_convert[input_num % 16] + hex_digit
    else:
        hex_digit = str(input_num % 16) + hex_digit
    input_num = division

print(hex_digit)

# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
user_input = input('Введите строку: ')
flag = None

for char in '.', ',', '/':
    if user_input.count(char) == 1:
        user_input = user_input.replace(char, '')
        flag = user_input.isdigit()
        break
    else:
        flag = False

print(f'Строка - это дробное число? - {flag}')


# 3.12 Вводим с клавиатуры строку. Необходимо развернуть подстроку между первой и последней буквой "о".
# Если она только одна или её нет, сообщить, что буква "о" -одна или не встречается
user_str = input('Введите строку: ')

if 'о' in user_str and user_str.count('о') > 1:
    o_pos1 = user_str.find('о')
    o_pos2 = user_str.rfind('о')
    new_str = user_str[:o_pos1 + 1] + user_str[o_pos2 - 1: o_pos1: -1] + user_str[o_pos2:]
    print(new_str)
else:
    print('Буква "о" одна или не встречается')
