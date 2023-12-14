# Machine Learning

# REST API ML

## Introduction

This API provides endpoints to recomendation, prediction and financial literacy

<br>_Demo : 

## Recomendation saham Endpoints

### 

- **Endpoint:** `/recomendation`
- **Method:** `POST`
- **Description:** Financial product recommendations based on user income and expenses.
- **Body:**
  ```json
  {
    "pemasukan_seminggu": [50000, 80000, 40000, 45000, 90000, 80000, 75000],
    "pengeluaran_seminggu": [70000, 30000, 45000, 45000, 93000, 77000, 80000]
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
      'Pemasukan User': [40000, 1000, 2000, 2000, 3000, 4000, 5000],
      'Pengeluaran User': [400000, 10000, 20000, 20000, 30000, 40000, 500000],
      'recomendations': "Tidak ada rekomendasi Saham, Pengeluaran anda terlalu banyak"
  }
  ```
  
no key authentication



## Recomendation and prediction expense

### 

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** provides user spending recommendations based on algorithm predictions
- **Body:**
  ```json
  {
    "pengeluaran_seminggu": [70000, 30000, 45000, 45000, 93000, 77000, 80000]
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
    'histories Pengeluaran User': [70000, 30000, 45000, 45000, 93000, 77000, 80000],
    'prediksi pengeluaran besok': 50000,
    'rekomendasi pengeluaran': 50000
  }
  ```
  
no key authentication



## Financial related articles and news

### 

- **Endpoint:** `/news`
- **Method:** `GET`
- **Description:** Providing all the news and literacy about finance, investment and stock recommendations from Indonesia.
  
no key authentication
