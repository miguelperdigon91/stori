from model.balance_detail_model import BalanceDetail


class ModelManager:
    @staticmethod
    def balance_detail(_id: int, date: str, transaction: float, month: str):
        return BalanceDetail(_id, date, transaction, month)
