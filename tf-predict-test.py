import requests

url = 'https://savemoney-flask-rdiyde43ea-uc.a.run.app/predict'

user = {
    "expense": [150000,  200000,  100000,  120000, 125000,  80000,  90000]
}

response = requests.post(url, json=user).json()
print(response)