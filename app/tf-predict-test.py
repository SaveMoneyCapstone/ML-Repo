import requests

url = 'http://localhost:9696/predict'

user = {
    "pengeluaran_seminggu": [150000,  200000,  100000,  120000, 125000,  80000,  90000]
}

response = requests.post(url, json=user).json()
print(response)