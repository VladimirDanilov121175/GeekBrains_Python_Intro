# ****************************************************************
# Морской бой
# ****************************************************************

from random import randint

# Create a sea area
sea = [['.\t' for _ in range(5)] for _ in range(5)]


# Output of current state on the battlefield
def show_battlefield():
    for e in sea:
        for j in e:
            print(j, end='')
        print()


show_battlefield()

# Create 4 ships
ships = [(randint(0, 4), randint(0, 4))]
while len(ships) < 4:
    ship = (randint(0, 4), randint(0, 4))
    if ship not in ships:
        ships.append(ship)

ship_count = len(ships)
torpedo_count = 0
previous_shots = []


def check_range(coordinates):

    # if only one coordinate inputted
    while len(coordinates) < 3:
        coordinates = input('Координаты должны состоять из 2 значений! Повтори ввод: ')

    spl = coordinates.split()
    tup = tuple(map(int, spl))  # convert str to int

    # if inputs are out of range
    while tup[0] > 4 or tup[1] > 4:
        new_input = input('Координаты должны быть в диапазоне от 0 до 4! Повтори ввод: ')
        tup = check_range(new_input)

    return tup


while ship_count:
    # print(ships)
    user_try = input('\nТвой выстрел! Введите координаты от 0 до 4 через пробел: ')
    user_try = check_range(user_try)
    if user_try in previous_shots:
        print('Такой выстрел уже был!')
    elif user_try in ships:
        ship_count -= 1
        sea[user_try[0]][user_try[1]] = '[X]\t'
        print(f'Попал! Осталось {ship_count} кораблей.')
    else:
        sea[user_try[0]][user_try[1]] = '*\t'
        print(f'Мимо!')
    torpedo_count += 1
    previous_shots.append(user_try)
    show_battlefield()
else:
    print(f'\nПобеда! Все корабли противника затоплены!\n'
          f'Расход {torpedo_count} торпед')
