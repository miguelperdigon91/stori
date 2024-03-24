from repository.balance_detail_repo import BalanceDetailRepo


class Config:
    def __init__(self):
        self._balance_detail_repo = BalanceDetailRepo()

    def init(self):
        self._balance_detail_repo.create_table()
        self._balance_detail_repo.delete_all()
