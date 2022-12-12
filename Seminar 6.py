"""
1)Правильной скобочной последовательностью называется строка, состоящая только из символов «скобки»
(открывающих "(" и закрывающих ")"), где каждой закрывающей скобке найдётся соответствующая открывающая.
Например, () и (()()) — правильные последовательности, а (()(() или )( — нет.

Напишите функцию , которая проверяет, является ли поступившая на вход строка правильной скобочной последовательностью.
Если да, она должна печатать YES, в противном случае — NO. Обратите внимание, что пустая строка также является
правильной скобочной последовательностью.
"""
# def right_sequence(symb):
#     length = len(symb)
#     if length % 2 == 0 and symb[0] == '(' and symb[-1] == ')':
#         count_open = symb.count('(')
#         count_closed = symb.count(')')
#
#         if count_open == count_closed:
#             return 'Yes'
#     else:
#         return "No"
#
#
# my_str = '())))((()'
# result = right_sequence(my_str)
# print(result)

# 2) Требуется по запросу выдавать N различных паролей длиной M символов, состоящих из строчных
# и прописных латинских букв # и цифр, кроме тех, которые легко перепутать между собой: «l» (L маленькое),
# «I» (i большое), «1» (цифра), «o» и «O» # (большая и маленькая буквы) и «0» (цифра).
#
# Решение должно содержать две функции: вспомогательную generate_password(m), возвращающую случайный пароль
# длиной m символов, и основную main(n, m), возвращающую список из n различных паролей, каждый длиной m символов.

from random import randint

# Methods for generating passwords
def generate_password(p_length):

    # Generating random proportions of chars and digits in the password
    digs_number = p_length - randint(2, p_length - 1)  # 2 cause at least one lower and one upper case to preserve
    p_length -= digs_number
    uppers_number = p_length - randint(1, p_length - 1)   # randomizing number of upper case chars
    lowers_number = p_length - uppers_number   # rest for lower case chars

    password = []

    # Adding lower case chars
    for _ in range(lowers_number):
        rand = randint(0, len(low_chars) - 1)
        password.append(low_chars[rand])

    # Inserting upper case chars into random positions
    for _ in range(uppers_number):
        rand = randint(0, len(password))
        char = up_chars[randint(0, len(low_chars) - 1)]
        password.insert(rand, char)

    for _ in range(digs_number):
        rand = randint(0, len(password))
        password.insert(rand, randint(2, 9))

    return ''.join(str(i) for i in password)


low_chars = [_ for _ in 'abcdefghijkmnpqrstuvwxyz']
up_chars = [_ for _ in 'ABCDEFGHJKLMNPQRSTUVWXYZ']

m = int(input("How many symbols should contain the password? >>> "))

flag = input('Generate a random password? y/n >>> ')
if flag == 'y':
    print(generate_password(m))
else:
    for _ in range(int(input("How many passwords do you want to generate? >>> "))):
        print(generate_password(m))
