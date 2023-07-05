# Dockerfile
FROM python:3.9

WORKDIR /app

COPY app/app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]