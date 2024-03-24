class BalanceReport:
    def __init__(self, total: float, avg_debt: float, avg_credit: float, counter_transactions: dict):
        self.total = total
        self.avg_debt = round(avg_debt, 2)
        self.avg_credit = round(avg_credit, 2)
        self.counter_transactions = counter_transactions

    def get_total(self):
        return self.total

    def get_avg_debt(self):
        return self.avg_debt

    def get_avg_credit(self):
        return self.avg_credit

    def get_counter_transactions(self):
        return self.counter_transactions
