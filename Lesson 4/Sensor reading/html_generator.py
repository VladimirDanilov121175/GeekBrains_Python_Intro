from user_interface import view_temperature
from user_interface import view_pressure
from user_interface import view_wind_speed
from sensor_reading import data_collection


def create_html(device):
    style = 'style=font-size:25px'
    html = '<html>\n\t<head></head>\n\t<body>\n'
    html += '\t\t<p {}>Temperature: {} degree Celsius</p>\n'.format(style, view_temperature(device))
    html += '\t\t<p {}>Pressure: {} mmHg</p>\n'.format(style, view_pressure(device))
    html += '\t\t<p {}>Wind speed: {} m/sec</p>\n'.format(style, view_wind_speed(device))
    html += '\t</body>\n</html>'

    with open('index.html', 'w') as h:
        h.write(html)
        return html


def new_create_html(data):
    t, p, w = data
    style = 'style=font-size:25px'
    html = '<html>\n\t<head></head>\n\t<body>\n'
    html += '\t\t<p {}>Temperature: {} degree Celsius</p>\n'.format(style, t)
    html += '\t\t<p {}>Pressure: {} mmHg</p>\n'.format(style, p)
    html += '\t\t<p {}>Wind speed: {} m/sec</p>\n'.format(style, w)
    html += '\t</body>\n</html>'

    with open('new_index.html', 'w') as h:
        h.write(html)

    return data
