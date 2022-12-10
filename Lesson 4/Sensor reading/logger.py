from datetime import datetime


def log_temperature(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as log:
        log.write('{}: temperature {}\n'.format(time, data))


def log_pressure(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as log:
        log.write('{}: pressure {}\n'.format(time, data))


def log_wind_speed(data):
    time = datetime.now().strftime('%H:%M')
    with open("log.csv", "a") as log:
        log.write('{}: wind_speed {}\n'.format(time, data))
