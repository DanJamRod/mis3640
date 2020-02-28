import urllib.request
import json
import pprint

APIKEY = 'd7283dd1ae413b6d08441f2f07e6d36a'
city = 'Blidworth'
country_code = 'GB'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# How do we get current temperature?
temp = response_data["main"]["temp"]
print(f"The current temperature in DJR's hometown of {city}, {country_code} is {int(temp-273.15)}°C")