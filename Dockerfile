FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Ensure the .env file is copied into the Docker image
COPY .env /app/.env

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "funsol_vidPref.wsgi:application"]
