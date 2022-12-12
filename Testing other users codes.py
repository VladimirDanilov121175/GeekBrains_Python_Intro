from random import choice, randint

def generate_password(m, letters):
    password = ''
    what_was = []
    for i in range(m):
        what_is = randint(0, 2)
        what_was.append(what_is)
        if i == m - 3 and (0 in what_was) < 1 or (1 in what_was) < 1 or (2 in what_was) < 1:
            if (0 in what_was) < 1: what_is = 0
            elif (1 in what_was) < 1: what_is = 1
            else: what_is = 2
            what_was[len(what_was) - 1] = what_is 
        if what_is == 0: password += str(randint(2, 9))
        elif what_is == 1: 
            char = str(choice(letters))
            password += char.upper()
        else: password += choice(letters)
    return password

def main(n, m, arr):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m, arr))
    return passwords

def print_arr(arr):
    for i in arr:
        print(i)

count = int(input('Enter, how many passwords you need: '))
length = int(input('Enter, how long passwords must been: '))
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c', \
    'v', 'b', 'n', 'm']
print_arr(main(count, length, letters))