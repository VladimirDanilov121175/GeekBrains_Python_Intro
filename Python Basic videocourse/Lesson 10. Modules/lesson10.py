import os, sys
import random

# pl = sys.platform
#
# for i in range(1, 5):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(pl, i))
#     os.mkdir(new_path)
#
# for i in sys.path:
#     print(i)

# print(os.name)
# print(os.getcwd())
# print(sys.executable)

li = [123, 45, 95, 11, 20, 7, 43]


def random_choice(arr):
    return random.choice(arr)


# print(random_choice(li))
