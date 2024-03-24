from typing import List

from model.balance_detail_model import BalanceDetail
from repository.config.repository import Repository
from repository.config.queries_template import query_insert, query_select


class BalanceDetailRepo(Repository):
    def __init__(self):
        super().__init__(BalanceDetail)

    def insert_multi(self, balance_details: List[BalanceDetail]):
        ignore_first_element = 1

        query = self._build_insert_query(balance_details[0])
        for balance_detail in balance_details[ignore_first_element:]:
            query += ';' + self._build_insert_query(balance_detail)

        self._data_base.execute_query(query)

    def get_total_summary(self):
        total_field = "SUM(transaction) AS total"
        avg_debt_field = "AVG(CASE WHEN transaction >= 0 THEN transaction ELSE NULL END) AS avg_debt"
        avg_credit_field = "AVG(CASE WHEN transaction < 0 THEN transaction ELSE NULL END) AS avg_credit"

        query = query_select(
            self._table_name,
            '{},{},{}'.format(total_field, avg_debt_field, avg_credit_field),
            '')

        return self._data_base.do_query(query)[0]

    def count_transactions_by_month(self):
        query = query_select(self._table_name,
                             'COUNT(transaction), month',
                             'GROUP BY month'
                             )

        return self._data_base.do_query(query)

    def _build_insert_query(self, balance_detail: BalanceDetail):
        return query_insert(
            self._table_name,
            'id, date, transaction, month',
            "{}, '{}', {}, '{}'".format(
                balance_detail.id(),
                balance_detail.date(),
                balance_detail.transaction(),
                balance_detail.month()))
