FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]

