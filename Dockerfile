# Stage 1: Python Flask app
FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["main.py", ".flaskenv", "model_recomendation=2.bin", "model_cnn_lstm.h5", "./"]

EXPOSE 8080
ENV PORT 8080

# Specify entrypoint
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

CMD exec gunicorn --bind :$PORT main:app --workers 1 --threads 1 --timeout 1600