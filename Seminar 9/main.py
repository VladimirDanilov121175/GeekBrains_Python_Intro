import requests

API_key = '4321a3d417b53045aa1b6617c529c910'
city_name = 'Казань'
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru")


print(response.json())

temp = response.json()
temp1 = temp['main']
print(temp1['temp'])