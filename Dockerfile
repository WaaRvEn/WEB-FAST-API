# Usamos una base 'slim' (Debian), más fácil que Alpine
FROM python:3.12-slim

WORKDIR /code

# Instalamos dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

# IMPORTANTE: El host 0.0.0.0 es obligatorio para ver la web
CMD ["fastapi", "run", "main.py", "--port", "80", "--host", "0.0.0.0"]