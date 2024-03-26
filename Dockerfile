FROM python:3.8

COPY . /app

WORKDIR /app

RUN chmod +x /app/wait-for-it.sh
ENTRYPOINT [ "/bin/bash", "-c" ]
CMD ["./wait-for-it.sh", "db:5432"]

RUN pip install --no-cache-dir -r requirements.txt