# Stage 1: Python Flask app
FROM python:3.9-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8080
ENV PORT 8080

# Specify entrypoint
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app