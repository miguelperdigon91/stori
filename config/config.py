from repository.balance_detail_repo import BalanceDetailRepo
from source.database import DataBase


class Config:
    def __init__(self):
        self._data_base_connection = DataBase()
        self._balance_detail_repo = BalanceDetailRepo()

    def init(self):
        self._balance_detail_repo.create_table()
        self._balance_detail_repo.delete_all()

    def close(self):
        self._data_base_connection.close()
