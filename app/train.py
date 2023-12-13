import numpy as np
import pandas as pd
import json
import requests
import urllib.parse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import dill

def generate_saham_tren(api_url, api_key, requests, json, pd):
  API_URL_KODE = api_url
  headers = {"X-API-KEY": api_key}

  response = requests.get(API_URL_KODE, headers=headers).json()
  response_str = json.dumps(response)
  SYMBOL = pd.json_normalize(json.loads(response_str), record_path=['data', 'results'])
  SYMBOL = SYMBOL['symbol']

  SYMBOL_string = ','.join(SYMBOL)

  return SYMBOL_string

def transform_json_to_df(api_url, symbol, api_key, urllib, requests, json, pd):
  API_URL = api_url
  SYMBOL = symbol
  API_KEY = api_key

  query_params = urllib.parse.urlencode({'symbols': SYMBOL})
  new_url = API_URL + '?' + query_params

  url = new_url
  headers = {"X-API-KEY": API_KEY}

  response = requests.get(url, headers=headers).json()
  response_str = json.dumps(response)
  df = pd.json_normalize(json.loads(response_str), record_path=['data', 'results'])
  df = df[['company.name', 'company.logo', 'symbol', 'date', 'open', 'high', 'low', 'close', 'volume']]
  df["hasil_mean"] = df.apply(lambda x: (x["open"] + x["high"] + x["low"] + x["close"]) / 4, axis=1)
  return df


def model_function(df_json, tfidfvectorizer, cosine_similarity, pd):
  # Inisialisasi TfidfVectorizer
  tfv = tfidfvectorizer
  # Melakukan perhitungan idf pada data cuisine
  tfv.fit(df_json['hasil_mean'].astype(str))
  tfidf_matrix = tfv.fit_transform(df_json['hasil_mean'].astype(str))
  tfidf_matrix.todense()
  cosine_sim = cosine_similarity(tfidf_matrix)
  cosine_sim_df = pd.DataFrame(
    cosine_sim,
    columns=df_json['symbol'],
    index=df_json['symbol']
  )
  return cosine_sim_df

def transform_data(data_pemasukan, data_pengeluaran, data_saham, np):
  # Inisialisasi variabel testing
  # data pemasukan dan pengeluaran selama seminggu
  pemasukan_mean = np.sum(data_pemasukan) / len(data_pemasukan)
  pengeluaran_mean = np.sum(data_pengeluaran).mean() / len(data_pengeluaran)
  perbandingan = pemasukan_mean - pengeluaran_mean

  if (perbandingan < 0):
    return "Tidak ada rekomendasi Saham, Pengeluaran anda terlalu banyak"
  else:
    # Cari baris yang sesuai
    diff = perbandingan - data_saham["hasil_mean"]

    idx = diff <= 10

    actual_df = data_saham[idx]
    data_selected = actual_df['hasil_mean'].min()

    saham_selected = data_saham[data_saham.hasil_mean.eq(data_selected)]

    data_selected_saham = saham_selected.loc[:, 'symbol'].to_string(index=False)
    return data_selected_saham


# deploy

C = 1
output_file = f'model_recomendation={C}.bin'

f_out = open(output_file, 'wb')
dill.dump((generate_saham_tren, transform_json_to_df, transform_data, model_function), f_out)
f_out.close()
print("model saved")