import html_generator as hg
import xml_generator as xg
from sensor_reading import data_collection

# Точка входа в программу

print(hg.create_html(1))
# print(xg.create_xml(1))

# xg.new_create_xml(hg.new_create_html(data_collection(device=1)))
