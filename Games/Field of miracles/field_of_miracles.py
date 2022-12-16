"""****************************************************************
                        ПОЛЕ ЧУДЕС
****************************************************************"""
from random import randint
import random
import time
import sys


def rotate_drum():
    keys = [_ for _ in drum.keys()]
    # Randomizing algorithm
    rand = randint(0, 2)
    if rand == 0:
        sect = keys[randint(0, 4)]
    elif rand == 1:
        sect = keys[randint(0, 6)]
    else:
        sect = keys[randint(0, 8)]

    return sect


def animate_drum(key):
    for _ in range(5):
        for k in drum.keys():
            sys.stdout.write("\r")
            sys.stdout.write("\r{}".format(k))
            sys.stdout.flush()
            time.sleep(.1)

    sys.stdout.write('\r{}\n'.format(key))

    print(f'Ведущий: \t{drum[key]}\n')
    time.sleep(1)


def choose_question():
    keys = [_ for _ in quiz.keys()]
    # Randomizing algorithm
    q = keys[randint(0, len(keys)-1)]
    return q


def display_word(letter):
    global word
    word = word.replace(letter, letter.upper())
    for c in word:
        print('♦', end='') if c.islower() else print(c, end='')
    print(f'\n{quiz[question]}\n')
    time.sleep(2)


def guess_word(user, turn):
    if turn == 0:
        input('Ведущий: \t' + user1['name'] + ', крутите барабан! >>>')
    else:
        print('Игрок ' + user['name'] + ' крутит барабан...')
        time.sleep(1.5)

    sector = rotate_drum()
    animate_drum(sector)

    if sector in [100, 200, 400, 800, 1000]:
        display_word('')
        # Calling a letter or word
        if turn == 0:
            guess = input('Ведущий: \tНазовите слово целиком или букву >>> ').lower()
        else:
            guess = random.choice(alphabet.lower())
            print(user['name'] + f': буква "{guess.upper()}"')
            time.sleep(2)

        # if the whole word called
        if guess.lower() == question.lower():
            print(question.upper())
            print('Ведущий: \tИ перед нами победитель шоу "Поле чудес" - {}!!!'.format(user['name']))
            return 'game over'

        elif guess.lower() in question.lower() and guess.lower() not in used_chars:
            print('Ведущий: \tЕсть такая буква в этом слове! Откройте!\n')
            time.sleep(1)
            used_chars.append(guess)
            user['count'] += sector
            display_word(guess)
            if word.isupper():
                print('Ведущий: \tИ перед нами победитель шоу "Поле чудес" - {}!!!'.format(user['name']))
                return 'game over'
            else:
                return turn
        else:
            used_chars.append(guess)
            print('Ведущий: \tНе угадали! Ход переходит следующему участнику\n')
            time.sleep(2)
            if turn in [0, 1]:
                return turn + 1
            else:
                return 0

    elif sector == 'Сектор "Пропуск хода"':
        if turn in [0, 1]:
            return turn + 1
        else:
            return 0

    elif sector == 'Сектор "x2"':
        user['count'] *= 2
        return turn

    elif sector == 'Приз':
        print('Ведущий: \tАвтомобиль в студию!!!')
        time.sleep(3)
        return turn

    else:
        user['count'] = 0
        if turn in [0, 1]:
            return turn + 1
        else:
            return 0


# ****************************************************************
# Main part
# ****************************************************************
drum = {
        100: '100 очков на барабане!',
        200: '200 очков на барабане!',
        400: '400 очков на барабане!',
        800: '800 очков на барабане!',
        1000: '1000 очков на барабане!',
        'Сектор "Пропуск хода"': 'И в игру вступает следующий участник нашего шоу',
        'Сектор "x2"': 'Поздравляем! Ваши очки удваиваются!',
        'Приз': 'Сектор "ПРИИИИИИИЗ"!!!!',
        'Сектор "XXXX"': 'Все Ваши очки сгорели!!! Ход переходит к следующему участнику'
}

quiz = {
    'Камикадзе': 'С японского это слово переводится как «Божественный ветер»',
    'Вечность': 'С чем в шутку сравнивал Островский соленый огурец?',
    'Шарманка': 'Название этого инструмента произошло от первого слова песни, которая чаще всего на нем исполнялась',
    'Тюрьма': 'В качестве чего использовали баобабы в XIX веке в Австралии?',
    'Сковорода': 'Что использовали в Китае для глажки белья вместо утюга?',
    'Буревестник': 'В словаре Владимира Ивановича Даля встречается старинное название барометра. Какое?'
}

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
used_chars = []

question = choose_question()
word = question.lower()

print('Начинаем капитал-шоу "Поле чудес"!')
user1 = {'name': input("Как Вас зовут? >>> "), 'count': 0}
user2 = {'name': 'Сергей', 'count': 0}
user3 = {'name': 'Ирина', 'count': 0}
names = [user1['name'], user2['name'], user3['name']]


print('Против Вас сегодня играют {} и {}\n'.format(user2['name'], user3['name']))
time.sleep(1)
print(f'Итак, перед вами слово, состоящее из {len(word)} букв.')
print('♦'*len(word))
time.sleep(2)
print(f'\nВопрос звучит следующим образом:\n{quiz[question]}\n')
time.sleep(3)

# Who's first
turn = randint(0, 2)
print(f'И первым крутит барабан {names[turn]}\n')

flag = True
while flag:
    if turn == 0:
        turn = guess_word(user1, turn)
    elif turn == 1:
        turn = guess_word(user2, turn)
    elif turn == 2:
        turn = guess_word(user3, turn)
    else:
        print('GAME OVER')
        flag = False
