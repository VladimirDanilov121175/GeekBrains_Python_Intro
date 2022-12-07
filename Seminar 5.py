from random import randint

# Игра "Камень, ножницы, бумага"


user = input('Что у вас: ')

sign = ['камень', 'ножницы', 'бумага']
i = randint(0, 2)
comp = sign[i]

print(user, comp)

flag = True


if user == 'ножницы' and comp == 'камень': flag = False
if user == 'камень' and comp == 'бумага': flag = False
if user == 'бумага' and comp == 'ножницы': flag = False

if flag:
    if user == comp:
        print('Ничья')
    else:
        print ("Вы победили")
else: print ("Победил компьютер")
