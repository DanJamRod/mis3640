import pprint
weather = {'coord': {'lon': -71.29, 'lat': 42.3}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 278.47, 'feels_like': 268.93, 'temp_min': 275.93, 'temp_max': 281.15, 'pressure': 992, 'humidity': 45}, 'visibility': 16093, 'wind': {'speed': 9.8, 'deg': 280, 'gust': 15.9}, 'clouds': {'all': 90}, 'dt': 1582831683, 'sys': {'type': 1, 'id': 5255, 'country': 'US', 'sunrise': 1582802683, 'sunset': 1582842694}, 'timezone': -18000, 'id': 4954738, 'name': 'Wellesley', 'cod': 200}
pprint.pprint(weather)

# what is current temperature?
city = weather["name"]
country_code = weather["sys"]["country"]
temp = weather["main"]["temp"]
print(f"The current temperature at Babson College in {city}, {country_code} is {int(temp-273.15)}°C")