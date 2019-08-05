import requests

API_ENDPOINT = "http://localhost:5000/predict"

data = "data array"

r = requests.post(API_ENDPOINT, json = {'data': data})

print(r.text)