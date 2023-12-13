from urllib import response
import numpy as np
import pandas as pd
import json
import requests
import urllib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import dill
from flask import Flask, request, jsonify
import os
import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
import numpy as np
from proto import np_to_protobuf

# os.environ["no_proxy"] = "*"
# os.getenv("no_proxy")

API_URL = "https://api.goapi.io/stock/idx/prices"
API_KEY = '31929822-ee03-533e-38b4-5d817145'
SYMBOL_URL = "https://api.goapi.io/stock/idx/trending"


# model recomendation
input_file = 'model_recomendation=1.bin'

tfidfvectorizer = TfidfVectorizer()

with open(input_file, 'rb') as f_in:
    generate_saham_tren, transform_json_to_df, transform_data, model = dill.load(f_in)

symbol_string = generate_saham_tren(SYMBOL_URL, API_KEY, requests, json, pd)
data_saham = transform_json_to_df(API_URL, symbol_string, API_KEY, urllib, requests, json, pd)
model = model(data_saham, tfidfvectorizer, cosine_similarity, pd)


# model forecast
host = os.getenv('TF_SERVING_HOST', 'localhost:8500')
channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()

    pb_request.model_spec.name = 'model_cnn_lstm'
    pb_request.model_spec.signature_name = 'serving_default'

    pb_request.inputs['input_7'].CopyFrom(np_to_protobuf(X))
    return pb_request

def prepare_response(pb_response):
    preds = pb_response.outputs['dense_170'].float_val
    return preds[0]

def predict(data):
    X = np.array([data])
    X_float = X.astype(np.float32)
    pb_request = prepare_request(X_float)
    pb_response = stub.Predict(pb_request)
    response = prepare_response(pb_response)
    return response


#  endpoint news
kategori = "market"
url_news = f"https://api-berita-indonesia.vercel.app/cnbc/{kategori}"

response_news = requests.get(url_news)

app = Flask('model')

@app.route('/recomendation', methods=['POST'])
def saham_recommendations():
    if request.method == "POST":
        items = data_saham
        k = 10
        data_user = request.get_json()
        data_pemasukan = data_user['pemasukan_seminggu']
        data_pengeluaran = data_user['pengeluaran_seminggu']
        if (len(data_pemasukan) == 7 and len(data_pengeluaran) == 7):

            # pengeluaran user = hasil mean pemasukan dan pengeluaran
            pengeluaran_user = transform_data(data_pemasukan, data_pengeluaran, data_saham, np)
            if pengeluaran_user == "Tidak ada rekomendasi Saham, Pengeluaran anda terlalu banyak":
                return jsonify({
                    "status": {
                        "code": 200,
                        "message": "Success recomendation"
                    },
                    "data": {
                        'Pemasukan User': data_pemasukan,
                        'Pengeluaran User': data_pengeluaran,
                        'recomendations': "Tidak ada rekomendasi Saham, Pengeluaran anda terlalu banyak"
                    }
                }), 200
            else:
                index = model.loc[:,pengeluaran_user].to_numpy().argpartition(range(-1, -k, -1))
                closest = model.columns[index[-1:-(k+2):-1]]

                df_recomendations = pd.DataFrame(closest).merge(items).head(k)
                
                recomendations = json.dumps(df_recomendations.to_dict(orient='records'))

                return jsonify({
                    "status": {
                        "code": 200,
                        "message": "Success recomendation"
                    },
                    "data": {
                        'Pemasukan User': data_pemasukan,
                        'Pengeluaran User': data_pengeluaran,
                        'recomendations': json.loads(recomendations)
                    }
                }), 200
        else:
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Invalid length data. Please data containts a array = 7."
                },
                "data": "Tidak ada Rekomendasi Saham",
            }), 400
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": None,
        }), 405


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    if request.method == "POST":
        data = request.get_json()
        url = data['pengeluaran_seminggu']  
        if len(url) == 7:
            result = predict(url)
            if result <= url[-1]: 
                return jsonify({
                    "status": {
                        "code": 200,
                        "message": "Success recomendation and predict"
                    },
                    "data": {
                        'histories Pengeluaran User': list(url),
                        'prediksi pengeluaran besok': round(result),
                        'rekomendasi pengeluaran': round(result)
                    }
                }), 200
            else:

                total = sum(url) / len(url)

                data_recomen = round(abs(total - url[-1] - round(result)))

                return jsonify({
                    "status": {
                        "code": 200,
                        "message": "Success recomendation and predict"
                    },
                    "data": {
                        'histories Pengeluaran User': list(url),
                        'prediksi pengeluaran besok': round(result),
                        'rekomendasi pengeluaran': round(data_recomen)
                    }
                }), 200
        else:
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Invalid length data. Please data containts a array = 7."
                },
                "data": None,
            }), 400
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": "Tidak ada rekomendasi Saham",
        }), 405


@app.route('/news', methods=['GET'])
def news_endpoint():
    if request.method == "GET":
        return jsonify({
            "status": {
                "code": 200,
                "message": "Success get news"
            },
            "data": {
                'news': response_news.json()['data']
            }
        }), 200
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": None,
        }), 405


if __name__ == "model":
    app.run(debug=True, host='0.0.0.0', port=9696)