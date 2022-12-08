
if user_try in previous_shots:
    print('Такой выстрел уже был!')
torpedo_count += 1
continue

elif user_try in single_ships:
ship_count -= 1
sea[user_try[0]][user_try[1]] = '[X]\t'
print(f'Убит! Осталось кораблей: {ship_count}.')

elif user_try in used_squares:
for el in double_ships:
    if user_try in el.values():
        sea[user_try[0]][user_try[1]] = '[X]\t'  # Setting X over nuked ship
        el['hits'] += 1
        if el['hits'] == 2:
            ship_count -= 1
            print(f'Убит! Осталось кораблей: {ship_count}.')
        else:
            print('Ранен!')
else:
sea[user_try[0]][user_try[1]] = '*\t'
print('Missed')