import pickle
import json

my_favourite_group = {
    'name': 'Г.М.О',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]
}

print(my_favourite_group)
print(type(my_favourite_group))

j_group = json.dumps(my_favourite_group, ensure_ascii=False, indent=4)
print(j_group)
print(type(j_group))

p_group = pickle.dumps(my_favourite_group)
print(p_group)
print(type(p_group))

with open('group.json', 'w', encoding='utf-8') as j:
    json.dump(my_favourite_group, j, ensure_ascii=False)

with open('group.pickle', 'wb') as p:
    pickle.dump(my_favourite_group, p)
