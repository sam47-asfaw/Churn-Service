# Define base image
FROM python:3.11-slim

# Set working directory for the project
WORKDIR /app

# Create Conda environment from the YAML file
COPY requirements.txt .

# Activate the environment, and make sure it's activated:
RUN pip install -r requirements.txt

COPY ["model_C=1.0.bin", "predict.py", "./"]

EXPOSE 8080

CMD [ "waitress-serve", "--port=8080", "predict:app"]

