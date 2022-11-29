# 3.1 Вводим с клавиатуры десятичное число. Необходимо перевести его в двоичную систему счисления.
num = int(input("Enter a number: "))
div = None
res = ''

while num != 0:
    div = num // 2
    res = str(num - div * 2) + res
    num = div
print(res)

# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.
text = input('Введите текст: ')
vowel_list = 'аеиоуыэюяАЕИОУЫЭЮЯ'
exclusion_list = ',: ;?!-'
count_vowel = 0
count_s = 0


for c in text:
    if c in vowel_list:
        count_vowel += 1
    elif c not in exclusion_list:
        count_s += 1
print(f'Гласных - {count_vowel}')
print(f'Согласных - {count_s}')


# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом
text = (input('Введите текст или словосочетание: ')).lower()
text_inverse = text[::-1].lower()
if text_inverse == text:
    print("Слово является полиндромом")
else:
    print("Слово не является полиндромом")

# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами
text = input('Введите текст, слово или словосочетание: ')
length = len(text)
half = length // 2
print(text[half:] + text[:half])

# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре
text = input('Введите текст, слово или словосочетание: ')
count = 0
for c in text:
    if c.isupper(): count += 1
print('Uppercase count: %d' % count)

"""
3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать - безопасный он или нет. Безопасным считается,
если он от 8 символов, есть верхний и нижний регистр. А так же цифры. Можно, при желании, добавить и спец. символы
"""
password = input('Create a password: ')
spec_symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
c1, c2, c3, c4 = (None,) * 4

for char in password:
    if char in spec_symbols: c1 = 1
    if char.isdigit(): c2 = 1
    if char.isupper(): c3 = 1
    if char.islower(): c4 = 1
if c1 and c2 and c3 and c4 \
        and len(password) > 8:
    print('Пароль безопасный')
else:
    print('Пароль не безопасен!\n'
          'Безопасный пароль должен быть длиною не менее 8 знаков, содержать цифры, '
          'буквы верхнего и нижнего регистров, а также спецсимволы.')

# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего
text = input('Введите текст, слово или словосочетание: ')
max_count = 0
winner = None

for c in text:
    if text.count(c) > max_count:
        max_count = text.count(c)
        winner = c
        if winner == ' ': winner = 'пробела'
print(f'Чаще всего в данной строке встречается символ {winner} - {max_count} раз.')

# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
text = input('Введите текст, слово или словосочетание: ')

b = text.find('в')
print(text.find('в', b + 1))
