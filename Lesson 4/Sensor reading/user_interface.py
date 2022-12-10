from sensor_reading import get_temperature
from sensor_reading import get_pressure
from sensor_reading import get_wind_speed
import logger as log


def view_temperature(device):
    data = get_temperature(device)
    log.log_temperature(data)
    return data


def view_pressure(device):
    data = get_pressure(device)
    log.log_pressure(data)
    return data


def view_wind_speed(device):
    data = get_wind_speed(device)
    log.log_wind_speed(data)
    return data
