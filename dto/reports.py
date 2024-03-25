class BalanceReport:
    def __init__(self, total: float, avg_debt: float, avg_credit: float, counter_transactions: dict):
        self._total = total
        self._avg_debt = round(avg_debt, 2)
        self._avg_credit = round(avg_credit, 2)
        self._counter_transactions = counter_transactions

    def get_total(self):
        return self._total

    def get_avg_debt(self):
        return self._avg_debt

    def get_avg_credit(self):
        return self._avg_credit

    def get_counter_transactions(self):
        return self._counter_transactions
