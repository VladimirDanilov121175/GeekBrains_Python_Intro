import requests
from pprint import pprint

API_key = '4321a3d417b53045aa1b6617c529c910'
city_name = 'Чебоксары'
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&lang=ru&appid={API_key}")


pprint(response.json())

temp = response.json()
temp1 = temp['weather'][0]
print(temp1['description'])
