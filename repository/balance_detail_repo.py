from typing import List

from model.balance_detail_model import BalanceDetail
from repository.config.repository import Repository
from repository.config.queries_template import query_insert_many


class BalanceDetailRepo(Repository):
    def __init__(self):
        super().__init__('BalanceDetails', ['id', 'date', 'transaction', 'month'])

        self._id = 0
        self._month = 1
        self._transaction = 2
        self._month = 3

    def insert_multi(self, data: List[BalanceDetail]):
        values_to_insert = self._build_values(data)

        query = query_insert_many(
            self._table_name,
            '{}, {}, {}, {}'.format(self._get_field_name(self._id),
                                    self._get_field_name(self._month),
                                    self._get_field_name(self._transaction),
                                    self._get_field_name(self._month)),
            values_to_insert)

        self._data_base.execute_query(query)

    @staticmethod
    def _build_values(data: List[BalanceDetail]):
        result = ''

        for balance in data:
            tuple_str = "({}, '{}', {}, '{}')".format(
                balance.id(),
                balance.date(),
                balance.transaction(),
                balance.month())

            result += tuple_str

        return result
