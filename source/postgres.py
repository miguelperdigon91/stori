from psycopg2 import connect
from logging import error


class Postgres:
    def __init__(self, host, user, dbname, password):
        self._conn = connect('host={host} dbname={dbname} user={user} password={password}'.format(
            host=host,
            user=user,
            dbname=dbname,
            password=password
        ))

    def do_query(self, query):
        try:
            cursor = self._conn.cursor()
            cursor.execute(query)
            self._conn.commit()
            return cursor.fetchall()
        except Exception as e:
            error(str(e))

    def execute_query(self, query):
        try:
            cursor = self._conn.cursor()
            cursor.execute(query)
            self._conn.commit()
        except Exception as e:
            error(str(e))

    def close_conn(self):
        try:
            self._conn.close()
        except Exception as e:
            error(str(e))
