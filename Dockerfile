FROM python:3.8

RUN apt-get update \
    && apt-get install -y postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

RUN pip install psycopg2

COPY ./story-main /story-main

WORKDIR /story-main

CMD ["python", "main.py"]