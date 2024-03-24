class BalanceDetail:
    _id: int
    _date: str
    _transaction: float
    _month: str

    def __init__(self, _id: int, date: str, transaction: float, month: str):
        self._id = _id
        self._date = date
        self._transaction = transaction
        self._month = month

    def id(self):
        return self._id

    def date(self):
        return self._date

    def transaction(self):
        return self._transaction

    def month(self):
        return self._month
