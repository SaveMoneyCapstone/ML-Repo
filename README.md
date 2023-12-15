# Machine Learning

# REST API ML

## Introduction

This API provides endpoints to recomendation, prediction and financial literacy

<br>_Demo : https://savemoney-flask-rdiyde43ea-uc.a.run.app/

## Setup if we to local test
``` git clone https://github.com/SaveMoneyCapstone/ML-Repo.git ```

``` docker build -t api-model:v1 -f Dockerfile . ```

``` docker run -it --rm -p 8080:8080 api-model:v1 ```

## Test using script

``` python3 -m ensurepip ``` or ``` python -m ensurepip ``` 


``` pip install requests ```


### For Recomendation saham Endpoints
Open file ```predict-test.py```
```python
  url = 'http://localhost:9696/recomendation'

  user = {
    "incomes": [50000, 80000, 40000, 45000, 90000, 80000, 75000],
    "expense": [70000, 30000, 45000, 45000, 93000, 77000, 80000]
  }  

  response = requests.post(url, json=user).json()
  print(response)
```
Replace url to domain --> https://savemoney-flask-rdiyde43ea-uc.a.run.app/recomendation
Run ``` python predict-test.py ```

### For Recomendation and prediction expense
Open file ```tf-predict-test.py```
```python
  import requests

  url = 'http://localhost:9696/predict'

  user = {
    "expense": [150000,  200000,  100000,  120000, 125000,  80000,  90000]
  }

  response = requests.post(url, json=user).json()
  print(response)
```
Replace url to domain --> https://savemoney-flask-rdiyde43ea-uc.a.run.app/predict
Run ``` python tf-predict-test.py ```


## Recomendation saham Endpoints

### 

- **Endpoint:** `/recomendation`
- **Method:** `POST`
- **Description:** Financial product recommendations based on user income and expenses.
- **Content-Type:** application/json
- **Body:**
  ```json
  {
    "incomes": [50000, 80000, 40000, 45000, 90000, 80000, 75000],
    "expense": [70000, 30000, 45000, 45000, 93000, 77000, 80000]
  }
  ```
- **Response:**
  ```json
    {
    "data": {
        "Pemasukan User": [
            50000,
            80000,
            40000,
            45000,
            90000,
            80000,
            75000
        ],
        "Pengeluaran User": [
            70000,
            30000,
            45000,
            45000,
            93000,
            77000,
            80000
        ],
        "recomendations": [
            {
                "close": 2900,
                "company.logo": "https://s3.goapi.id/logo/AMRT.jpg",
                "company.name": "Sumber Alfaria Trijaya Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 2885.0,
                "high": 2910,
                "low": 2840,
                "open": 2890,
                "symbol": "AMRT",
                "volume": 19292100
            },
            {
                "close": 5550,
                "company.logo": "https://s3.goapi.id/logo/BBRI.jpg",
                "company.name": "Bank Rakyat Indonesia (Persero) Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 5493.75,
                "high": 5550,
                "low": 5425,
                "open": 5450,
                "symbol": "BBRI",
                "volume": 270760600
            },
            {
                "close": 486,
                "company.logo": "https://s3.goapi.id/logo/BBYB.jpg",
                "company.name": "Bank Neo Commerce Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 464.5,
                "high": 494,
                "low": 438,
                "open": 440,
                "symbol": "BBYB",
                "volume": 605238300
            },
            {
                "close": 5350,
                "company.logo": "https://s3.goapi.id/logo/BBNI.jpg",
                "company.name": "Bank Negara Indonesia (Persero) Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 5300.0,
                "high": 5400,
                "low": 5225,
                "open": 5225,
                "symbol": "BBNI",
                "volume": 91435600
            },
            {
                "close": 178,
                "company.logo": "https://s3.goapi.id/logo/BRMS.jpg",
                "company.name": "Bumi Resources Minerals Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 176.0,
                "high": 182,
                "low": 172,
                "open": 172,
                "symbol": "BRMS",
                "volume": 302825500
            },
            {
                "close": 5950,
                "company.logo": "https://s3.goapi.id/logo/BMRI.jpg",
                "company.name": "Bank Mandiri (Persero) Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 5900.0,
                "high": 6025,
                "low": 5800,
                "open": 5825,
                "symbol": "BMRI",
                "volume": 189383100
            },
            {
                "close": 7200,
                "company.logo": "https://s3.goapi.id/logo/BREN.jpg",
                "company.name": "Barito Renewables Energy Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 7356.25,
                "high": 7625,
                "low": 7025,
                "open": 7575,
                "symbol": "BREN",
                "volume": 29173400
            },
            {
                "close": 101,
                "company.logo": "https://s3.goapi.id/logo/BIPI.jpg",
                "company.name": "Astrindo Nusantara Infrastruktur Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 101.25,
                "high": 103,
                "low": 100,
                "open": 101,
                "symbol": "BIPI",
                "volume": 600839300
            },
            {
                "close": 242,
                "company.logo": "https://s3.goapi.id/logo/WIKA.jpg",
                "company.name": "Wijaya Karya (Persero) Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 217.0,
                "high": 254,
                "low": 183,
                "open": 189,
                "symbol": "WIKA",
                "volume": 767534500
            },
            {
                "close": 2490,
                "company.logo": "https://s3.goapi.id/logo/ADRO.jpg",
                "company.name": "Adaro Energy Indonesia Tbk.",
                "date": "2023-12-14",
                "hasil_mean": 2475.0,
                "high": 2510,
                "low": 2440,
                "open": 2460,
                "symbol": "ADRO",
                "volume": 26268500
            }
        ]
    },
    "status": {
        "code": 200,
        "message": "Success recomendation"
    }
  }
  ```
  
if body data is not less or more than a list of 7
- **Response:**
  ```json
  {
    "code": 400,
    "message": "Invalid length data. Please data containts a array = 7."
  },
  "data": "Tidak ada Rekomendasi Saham",
  ```

if user expenses are more than income
- **Response:**
  ```json
  "status": {
      "code": 200,
      "message": "Success recomendation"
  },
  "data": {
      "Pemasukan User": [40000, 1000, 2000, 2000, 3000, 4000, 5000],
      "Pengeluaran User": [400000, 10000, 20000, 20000, 30000, 40000, 500000],
      "recomendations": "Tidak ada rekomendasi Saham, Pengeluaran anda terlalu banyak"
  }
  ```
  
no key authentication



## Recomendation and prediction expense

### 

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** provides user spending recommendations based on algorithm predictions
- **Content-Type:** application/json
- **Body:**
  ```json
  {
    "expense": [25000, 30000, 45000, 10000, 10000, 12000, 30000]
  }
  ```
- **Response:**
  ```json
    {
    "data": {
        "histories Pengeluaran User": [
            25000,
            30000,
            45000,
            10000,
            10000,
            12000,
            30000
        ],
        "prediksi pengeluaran besok": 9499,
        "rekomendasi pengeluaran": 9499
    },
    "status": {
        "code": 200,
        "message": "Success recomendation and predict"
    }
  }
  ```
  
if body data is not less or more than a list of 7
- **Response:**
  ```json
  {
    "code": 400,
    "message": "Invalid length data. Please data containts a array = 7."
  },
  "data": "Tidak ada Rekomendasi Saham",
  ```

if the prediction from the algorithm is smaller than the current spending
- **Response:**
  ```json
  "status": {
    "code": 200,
    "message": "Success recomendation and predict"
  },
  "data": {
    "histories Pengeluaran User": [70000, 30000, 45000, 45000, 93000, 77000, 80000],
    "prediksi pengeluaran besok": 50000,
    "rekomendasi pengeluaran": 50000
  }
  ```
  
no key authentication



## Financial related articles and news

### 

- **Endpoint:** `/news`
- **Method:** `GET`
- **Description:** Providing all the news and literacy about finance, investment and stock recommendations from Indonesia.
  
no key authentication
