FROM python:3.11-slim

# Dependencias de sistema para compilar mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecuta la app en 0.0.0.0:8080 (coincide con compose)
CMD ["python", "app.py"]
