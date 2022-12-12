from random import randint
import time

def animate_explosion():
    for char in '⋆*∎♦ ♦∎*⋆':
        print(char)
        time.sleep(.1)

animate_explosion()
