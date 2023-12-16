# Stage 1: Python Flask app
FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["main.py", ".flaskenv", "model_recomendation=2.bin", "model_cnn_lstm.h5", "./"]

EXPOSE 8080

# Specify entrypoint
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "main:app"]