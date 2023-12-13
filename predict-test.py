import requests

url = 'http://localhost:9696/recomendation'

user = {
    "pemasukan_seminggu": [50000, 80000, 40000, 45000, 90000, 80000, 75000],
    "pengeluaran_seminggu": [70000, 30000, 45000, 45000, 93000, 77000, 80000]
}

response = requests.post(url, json=user).json()
print(response)