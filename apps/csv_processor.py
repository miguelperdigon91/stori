from model.config.model_manager import ModelManager


class CSVProcessor:
    def __init__(self):
        self._model_manager = ModelManager()

    def process_transactions(self, transactions_df):
        transactions = []

        for row in transactions_df:
            transactions.append(self._model_manager.balance_detail(
                row[0],
                row[1],
                self._to_float(row[2]),
                self._extract_month(row[1])
            ))

        return transactions

    @staticmethod
    def _extract_month(date: str):
        return date.split('/')[0]

    @staticmethod
    def _to_float(value: str):
        value = value.replace('+', '')

        return float(value)
