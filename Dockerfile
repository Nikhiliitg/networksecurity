FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install -y awscli build-essential libssl-dev libffi-dev python3-dev

RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
