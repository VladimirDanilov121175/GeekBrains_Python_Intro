from user_interface import view_temperature
from user_interface import view_pressure
from user_interface import view_wind_speed
from sensor_reading import data_collection


def create_xml(device):
    xml = '<xml>\n'
    xml += '\t<temperature_view units = "degree Celsius">{}</temperature_view>\n' \
        .format(view_temperature(device))
    xml += '\t<pressure_view units = "mmHG">{}</pressure_view>\n' \
        .format(view_pressure(device))
    xml += '\t<wind_speed_view units = "mm/sec">{}</wind_speed_view>\n' \
        .format(view_wind_speed(device))
    xml += '</xml>'

    with open('data.xml', 'w') as x:
        x.write(xml)
        return xml


def new_create_xml(data):
    t, p, w = data
    t = t * 1.8 + 32    # Fahrenheit
    xml = '<xml>\n'
    xml += '\t<temperature_view units = "degree Fahrenheit">{}</temperature_view>\n' \
        .format(t)
    xml += '\t<pressure_view units = "mmHG">{}</pressure_view>\n' \
        .format(p)
    xml += '\t<wind_speed_view units = "mm/sec">{}</wind_speed_view>\n' \
        .format(w)
    xml += '</xml>'

    with open('new_data.xml', 'w') as x:
        x.write(xml)

    return data
