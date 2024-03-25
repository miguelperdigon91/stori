from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl
from logging import error
from os import environ
from typing import List


class EmailSender:
    @staticmethod
    def send(addressees: List[str], subject: str, body: str, is_html=False):
        try:
            gmail_user = 'miguelperdigon91@gmail.com'
            gmail_password = environ['GMAIL_PASSWORD']
            sent_from = 'technical_test@stori.com'
            to = addressees

            msg = MIMEMultipart()

            msg['From'] = gmail_user
            msg['To'] = ', '.join(addressees)
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain')) if not is_html else msg.attach(MIMEText(body, 'html'))

            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo()
                server.starttls(context=context)
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, msg.as_string())

            return True

        except Exception as e:
            error(str(e))
            return False
