from random import randint

# Imitating incoming data from sensors


def temperature(device):
    return randint(-20, 0) if device == 1 else randint(0, 20)


def pressure(device):
    return randint(750, 770) if device == 1 else randint(720, 750)


def wind_speed(device):
    return randint(10, 20) if device == 1 else randint(0, 9)
