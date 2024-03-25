import json

import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
#print(response)
print(json.dumps(response, indent=2))

for a in response:
    print(a["show"]["name"])

