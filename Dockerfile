FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

# Install common dependencies for Python packages
RUN apt update -y && \
    apt install -y awscli build-essential libssl-dev libffi-dev python3-dev git curl && \
    apt clean

# Install dependencies from requirements.txt
RUN pip install -v --no-cache-dir -r requirements.txt

# Set the command to run the application
CMD ["python3", "app.py"]
