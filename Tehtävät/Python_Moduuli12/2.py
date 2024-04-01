#API

import requests
import json

origin_url = "https://api.openweathermap.org/data/2.5/weather?q=Helsinki,fi&APPID=af99e58fadd43b9c804766c2f9e850ae"

response = requests.get(origin_url)

jsonResponse = json.loads(response.text)
print("Country: " + str(jsonResponse['sys']['country']))
print("City: " + str(jsonResponse['name']))
print("temperature: " + str(jsonResponse['main']['temp'] - 273) + " *C")
print("pressure: " + str(jsonResponse['main']['pressure']) + " paskal.")
print("humidity: " + str(jsonResponse['main']['humidity']) + " %")

"""
Country: FI
City: Helsinki
temperature: 8.769999999999982 *C
pressure: 990 paskal.
humidity: 77 %
"""


# https://www.youtube.com/watch?v=MS6fwU1DajI