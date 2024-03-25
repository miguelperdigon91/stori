FROM python:3.8

RUN apt-get update \
    && apt-get install -y postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_DB=Stori
ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432

ENV GMAIL_PASSWORD = ''

RUN service postgresql start &&\
    su -c 'psql -c "CREATE DATABASE Stori;"' postgres

RUN pip install --no-cache-dir -r requirements.txt

COPY ./story-main /story-main

WORKDIR /story-main

CMD ["python", "main.py"]