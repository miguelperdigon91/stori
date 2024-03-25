from source.postgres import Postgres
from os import environ


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class DataBase(metaclass=SingletonMeta):
    def __init__(self):
        self._postgres = Postgres(
            environ['POSTGRES_HOST'],
            environ['POSTGRES_USER'],
            environ['POSTGRES_DB'],
            environ['POSTGRES_PASSWORD'])

    def do_query_returning_id(self, query: str):
        return self._postgres.do_query(query)[0][0]

    def do_query(self, query: str):
        return self._postgres.do_query(query)

    def execute_query(self, query: str):
        self._postgres.execute_query(query)

    def close(self):
        self._postgres.close_conn()
