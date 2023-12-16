import requests

url = 'https://savemoney-flask-rdiyde43ea-uc.a.run.app/recomendation'

user = {
    "incomes": [50000, 80000, 40000, 45000, 90000, 80000, 75000],
    "expense": [70000, 30000, 45000, 45000, 93000, 77000, 80000]
}

response = requests.post(url, json=user).json()
print(response)