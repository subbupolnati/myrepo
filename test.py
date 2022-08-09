import requests
import json
query = {'lat':'45', 'lon':'180'}
response = requests.get('https://httpbin.org/get', params=query)
print(response.text)
