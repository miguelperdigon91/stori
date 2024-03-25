from apps.const import get_email_template
from dto.reports import BalanceReport
from repository.balance_detail_repo import BalanceDetailRepo


class ReportBuilder:
    def __init__(self):
        self._balance_detail_repo = BalanceDetailRepo()
        self._months_dict = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        }

    def build_balance_report(self):
        annual_data = self._balance_detail_repo.get_total_summary()
        monthly_data = self._balance_detail_repo.count_transactions_by_month()

        transactions = {}
        for row in monthly_data:
            month_name = self._months_dict[row[1]]

            transactions[month_name] = row[0]

        report = BalanceReport(annual_data[0], annual_data[1], annual_data[2], transactions)

        return self._build_message(report)

    @staticmethod
    def _build_message(report: BalanceReport):
        transaction_list = ''

        transactions_by_month = report.get_counter_transactions()
        for month in transactions_by_month:
            transaction_list += '<li>{}: {}</li>'.format(month, transactions_by_month[month])

        return get_email_template(report.get_total(), report.get_avg_credit(), report.get_avg_debt(), transaction_list)
