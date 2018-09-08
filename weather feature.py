import requests
from pprint import pprint
city = input("City Name:")
#url = api_address + city
url ='http://api.openweathermap.org/data/2.5/weather?q={}&appid=eb75bcb7f27a558426f5dc71d4ba6dbc&units=metric'.format(city)
json_data = requests.get(url)

data = json_data.json()
temp = data['main']['temp']

print('Temperature:', temp,'Degrees Celsius')
