#API

import requests
import json

origin_url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=af99e58fadd43b9c804766c2f9e850ae"

response = requests.get(origin_url)

jsonResponse = json.loads(response.text)
print("ulke: " + str(jsonResponse['sys']['country']))
print("sehir: " + str(jsonResponse['name']))
print("sicaklik: " + str(jsonResponse['main']['temp'] - 273) + " *C")
print("basinc: " + str(jsonResponse['main']['pressure']) + " paskal.")
print("nem orani: " + str(jsonResponse['main']['humidity']) + " %")

"""
ulke: GB
sehir: London
sicaklik: 12.339999999999975 *C
basinc: 995 paskal.
nem orani: 77 %
"""


# https://www.youtube.com/watch?v=MS6fwU1DajI