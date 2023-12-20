# Stage 1: Python Flask app
FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ["main.py", ".flaskenv", "model_recomendation=2.bin", "model_cnn_lstm.h5", "./"]

EXPOSE 8080
ENV PORT 8080

# Specify entrypoint
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app