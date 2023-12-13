# Stage 1: Python Flask app
FROM python:3.10-slim AS flask-app

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system --deploy

COPY main.py .flaskenv proto.py model_recommendation_1.bin /app/

EXPOSE 9696

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:9696", "main:app"]

# Stage 2: TensorFlow Serving
FROM tensorflow/serving:2.14.0

COPY --from=flask-app /app/model-forecast_tf-serving/model_cnn_lstm /models/model_cnn_lstm/1 

ENV MODEL_NAME="model_cnn_lstm"
