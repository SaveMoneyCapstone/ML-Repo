# Stage 1: Python Flask app
FROM python:3.10-slim AS flask-app

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["main.py", ".flaskenv", "proto.py", "model_recomendation=1.bin", "./"]

EXPOSE 9696

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:9696", "main:app"]

# Stage 2: TensorFlow Serving
FROM tensorflow/serving:2.14.0

COPY model-forecast_tf-serving/model_cnn_lstm /models/model_cnn_lstm/1 

ENV MODEL_NAME="model_cnn_lstm"
