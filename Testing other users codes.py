salary = int(input())
count_of_banknotes = 0
while(salary > 0):
    if salary > 25:
        print(f'25ти рублёвых купюр - {salary//25}')
        count_of_banknotes += salary//25
        salary %= 25
    elif salary >= 10:
        print(f'10ти рублёвых купюр - {salary//10}')
        count_of_banknotes += salary//10
        salary %= 10
    elif salary >= 7:
        print(f'7ми рублёвых купюр - {salary//7}')
        count_of_banknotes += salary//7
        salary %= 7
    elif salary >= 3:
        print(f'3х рублёвых купюр - {salary//3}')
        count_of_banknotes += salary//3
        salary %= 3
    else:
        print(f'рублёвых купюр - {salary//1}')
        count_of_banknotes += salary//1
        salary %= 1
print('Общее минимальное количество купюр = ', count_of_banknotes)