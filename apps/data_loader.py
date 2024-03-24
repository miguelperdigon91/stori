from apps.csv_processor import CSVProcessor
from apps.csv_reader import CSVReader
from repository.balance_detail_repo import BalanceDetailRepo


class DataLoader:
    def __init__(self):
        self._csv_reader = CSVReader()
        self._csv_processor = CSVProcessor()
        self._balance_detail_repo = BalanceDetailRepo()

    def load(self):
        transactions_df = self._csv_reader.read('transactions.csv')
        transactions = self._csv_processor.process_transactions(transactions_df)

        self._balance_detail_repo.insert_multi(transactions)

