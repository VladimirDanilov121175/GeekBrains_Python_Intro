from sensor_imitator import temperature
from sensor_imitator import pressure
from sensor_imitator import wind_speed


def get_temperature(device):
    return temperature(device)


def get_pressure(device):
    return pressure(device)


def get_wind_speed(device):
    return wind_speed(device)


def data_collection(device):
    data = (get_temperature(device), get_pressure(device), get_wind_speed(device))
    return data
