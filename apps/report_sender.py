from apps.email_sender import EmailSender
from apps.report_builder import ReportBuilder


class ReportSender:
    def __init__(self):
        self._email_sender = EmailSender()
        self._report_builder = ReportBuilder()

    def send(self):
        message = self._report_builder.build_balance_report()
        self._email_sender.send(['miguelperdigon91@gmail.com'], 'Financial Report of Stori', message, True)
