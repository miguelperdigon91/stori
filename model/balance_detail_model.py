class BalanceDetail:
    def __init__(self, _id: int, date: str, transaction: float, month: str):
        self._id: int = _id
        self._date: str = date
        self._transaction: float = transaction
        self._month: str = month

    def id(self):
        return self._id

    def date(self):
        return self._date

    def transaction(self):
        return self._transaction

    def month(self):
        return self._month
