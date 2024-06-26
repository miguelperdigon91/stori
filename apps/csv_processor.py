from model.config.model_manager import ModelManager


class CSVProcessor:
    def __init__(self):
        self._model_manager = ModelManager()

    def process_transactions(self, transactions_df):
        transactions = []

        for idx, row in enumerate(transactions_df.values):
            transactions.append(self._model_manager.balance_detail(
                idx,
                row[1],
                self._to_float(row[2]),
                self._extract_month(row[1])
            ))

        return transactions

    @staticmethod
    def _extract_month(date: str):
        date = date.replace('-', '/')

        return date.split('/')[0]

    @staticmethod
    def _to_float(value):
        if isinstance(value, float):
            if value != value:
                return 0
            return value

        value = value.strip()

        value = value.replace('+', '')
        value = value.replace(',', '.')

        return float(value)
