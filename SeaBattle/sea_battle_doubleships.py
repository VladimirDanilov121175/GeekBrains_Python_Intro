from random import randint
import time


def show_battlefield(count1, count2):
    print('\nТвое поле\t\t\t\tПоле противника')
    print(f'Кораблей: {count1}\t\t\t\tКораблей: {count2}\n')
    for e in sea:
        for j in e:
            print(j, end='\t')
        print()
    print()


# ****************************************************************
# Creating battlefield
# ****************************************************************
def create_battlefield():
    battlefield = [[' ']]
    for _ in range(2):
        for i in range(1, 6):
            battlefield[0].append(str(i))
        battlefield[0].append('\t')

    for i in 'ABCDE':
        battlefield.append([i])

    for i in range(2):
        for char in battlefield[1:]:
            if i == 0:
                for _ in range(5):
                    char.append('⋆')
                char.append(f'\t{char[0]}')
                for _ in range(5):
                    char.append('≈')
    return battlefield


# ****************************************************************
# creating ships
# ****************************************************************
def create_double_ships(shift):
    double_ships = []
    used_squares = []

    # Filling list with 2 double-squared ships

    while len(double_ships) < 2:
        # Creating a template for 2sqr-ships
        ship = {
            'square1': [],
            'square2': [],
            'hits': 0  # for counting hits while battle
        }

        # Randomizing coordinates for arrangement on the battlefield
        a, b = randint(1, 5), randint(1, 5) + shift
        if [a, b] not in used_squares:
            direction = randint(1, 4)  # randomizing in which direction to build the second square

            # Assigning the coordinates for the 1st and the 2nd squares
            ship['square1'] = [a, b]
            used_squares.append(ship['square1'])
            ship['square2'] = second_square(a, b, direction, shift, used_squares)
            used_squares.append(ship['square2'])
            double_ships.append(ship)

            if not shift:
                for ship in double_ships:
                    for el in ship['square1'], ship['square2']:
                        x, y = el
                        sea[x][y] = '[≡]'
    return [double_ships, used_squares]


# Function for building the second square
def second_square(x, y, direction, shift, used_list):
    if direction == 1:
        if y + 1 >= len(sea) + shift or [x, y + 1] in used_list:
            return second_square(x, y, 2, shift, used_list)
        else:
            return [x, y + 1]
    if direction == 2:
        if x + 1 >= len(sea) or [x + 1, y] in used_list:
            return second_square(x, y, 3, shift, used_list)
        else:
            return [x + 1, y]
    if direction == 3:
        if y - 1 - shift <= 0 or [x, y - 1] in used_list:
            return second_square(x, y, 4, shift, used_list)
        else:
            return [x, y - 1]
    if direction == 4:
        if x - 1 <= 0 or [x - 1, y] in used_list:
            return second_square(x, y, 1, shift, used_list)
        else:
            return [x - 1, y]


def create_single_ships(shift, used_list):
    single_ships = []
    while len(single_ships) < 4:
        s_ship = [randint(1, 5), randint(1, 5) + shift]
        if s_ship not in used_list:
            single_ships.append(s_ship)
            used_list.append(s_ship)

            if not shift:
                for ship in single_ships:
                    x, y = ship
                    sea[x][y] = '∎'
    return single_ships


def check_errors(coordinates):
    # if only one coordinate inputted
    while len(coordinates) < 2:
        coordinates = input('Координаты должны состоять из 2 значений! Повтори ввод: ')

    while coordinates[0].upper() not in 'ABCDE' or coordinates[1:] not in '12345':
        coordinates = input('Сперва буква А-Е, потом цифра 1-5! Повтори ввод: ')
    return coordinates


def user_shot(shift):
    global torpedo_count, comp_count, user_count, flag

    string = input('Твой выстрел! Введи координаты >>> ')
    string = check_errors(string)

    shot = ['.ABCDE'.find(string[0].upper()), int(string[1:]) + shift]
    # user_try = check_errors(user_try)
    print()

    if shot in user_previous_shots:
        print('Такой выстрел уже был!'.upper(), end=' ')
        return 'user'
    elif shot not in used_squares:
        x, y = shot
        sea[x][y] = '⋆'
        show_battlefield(user_count, comp_count)
        print('Промах! Переход хода.'.upper())
        torpedo_count += 1
        user_previous_shots.append(shot)
        return 'comp'
    elif shot in comp_sships:
        x, y = shot
        sea[x][y] = '♦'
        comp_count -= 1
        show_battlefield(user_count, comp_count)
        print(f'Есть попадание! Уничтожен однопалубный корабль.'.upper(), end=' ')

    else:
        for el in comp_dships[0]:
            if shot in el.values():
                x, y = shot
                sea[x][y] = '♦'
                el['hits'] += 1
                if el['hits'] == 2:
                    comp_count -= 1
                    show_battlefield(user_count, comp_count)
                    print(f'Двухпалубник уничтожен!'.upper(), end=' ')

                else:
                    show_battlefield(user_count, comp_count)
                    print('Есть попадание в двухпалубник!'.upper(), end=' ')

    torpedo_count += 1
    user_previous_shots.append(shot)
    return 'user'


def comp_shot():
    global comp_count, user_count, flag

    shot = [randint(1, 5), randint(1, 5)]
    while shot in comp_previous_shots:
        shot = [randint(1, 5), randint(1, 5)]

    conv = '.ABCDE'[shot[0]] + str(shot[1])
    print('Компьютер думает', end='')
    for i in range(5):
        time.sleep(.5)
        print('.', end='')

    if shot not in used_squares:
        x, y = shot
        sea[x][y] = '*'
        show_battlefield(user_count, comp_count)
        print(f'{conv} - Промах! Переход хода.'.upper())
        comp_previous_shots.append(shot)
        return 'user'

    elif shot in user_sships:
        user_count -= 1
        x, y = shot
        sea[x][y] = '♦'
        show_battlefield(user_count, comp_count)
        print(f'{conv} - О, нет! Противник уничтожил твой однопалубник (((.'.upper(), end=' ')
        time.sleep(.3)

    else:
        for el in user_dships[0]:
            if shot in el.values():
                x, y = shot
                sea[x][y] = '♦'
                el['hits'] += 1
                if el['hits'] == 2:
                    user_count -= 1
                    show_battlefield(user_count, comp_count)
                    print(f'{conv} - Двухпалубник уничтожен ((('.upper(), end=' ')
                else:
                    show_battlefield(user_count, comp_count)
                    print(f'{conv} - Полундра! Попадание в двухпалубник ((('.upper(), end=' ')
    comp_previous_shots.append(shot)
    time.sleep(4)
    return 'comp'


# *************************************************************
# Main part
# *************************************************************

sea = create_battlefield()

user_dships = create_double_ships(0)
comp_dships = create_double_ships(6)

used_squares = [i for i in user_dships[1]]
for i in comp_dships[1]:
    used_squares.append(i)

user_sships = create_single_ships(0, used_squares)
comp_sships = create_single_ships(6, used_squares)

# ****************************************************************
# Let's the battle begin!
# ****************************************************************
user_count = len(user_sships) + len(user_dships)
comp_count = len(comp_sships) + len(comp_dships)

torpedo_count = 0

user_previous_shots = []
comp_previous_shots = []

show_battlefield(user_count, comp_count)

flag = 'user'
while user_count and comp_count:
    if flag == 'user':
        flag = user_shot(shift=6)
    else:
        flag = comp_shot()

if not comp_count:
    print(f'\nПобеда! Все корабли противника потоплены!\n'
          f'Расход {torpedo_count} торпед')
else:
    print(f'\nКомпьютер в этот раз победил.\n'
          f'GAME OVER')
