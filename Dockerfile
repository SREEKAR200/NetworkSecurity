FROM python:4.15-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y && apt clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && pip install -r requirements.txt
CMD ["python3","app.py"]
