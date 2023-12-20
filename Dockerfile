# Define base image
FROM python:3.11-slim

# Set working directory for the project
WORKDIR /app

# Get dependencies
COPY requirements.txt .

# Download the dependencies:
RUN pip install -r requirements.txt

COPY ["model_C=1.0.bin", "predict.py", "./"]

EXPOSE 8080

CMD ["waitress-serve","--host=0.0.0.0","--port=8080","predict:app"]

