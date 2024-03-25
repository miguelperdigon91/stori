from apps.email_sender import EmailSender
from apps.report_builder import ReportBuilder
from os import environ


class ReportSender:
    def __init__(self):
        self._email_sender = EmailSender()
        self._report_builder = ReportBuilder()

    def send(self):
        message = self._report_builder.build_balance_report()
        self._email_sender.send([environ['EMAIL_TARGET']], 'Financial Report of Stori', message, True)
