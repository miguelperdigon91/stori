from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from unidecode import unidecode
from logging import error


class EmailSender:
    @staticmethod
    def send(destinataries, cc, subject, body, files, sender='ONE', is_html=False):
        try:
            gmail_user = Variable.get('{}_EMAIL'.format(sender))
            gmail_password = Variable.get('{}_EMAIL_PASSWORD'.format(sender))
            sent_from = Variable.get('{}_EMAIL'.format(sender))
            to = destinataries

            msg = MIMEMultipart()

            msg['From'] = gmail_user
            msg['To'] = ', '.join(destinataries)
            msg['CC'] = ', '.join(cc)
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain')) if not is_html else msg.attach(MIMEText(body, 'html'))

            for file_name in files:
                attachment = files[file_name]

                if type(attachment) is str:
                    file_name = attachment
                    attachment = open(attachment, 'rb')
                    attachment = attachment.read()
                else:
                    attachment = attachment.getvalue()

                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment)
                encoders.encode_base64(p)

                file_name = unidecode(file_name)
                p.add_header('Content-Disposition', 'attachment; filename= %s' % file_name)
                msg.attach(p)

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, msg.as_string())
            server.close()

            return True

        except Exception as e:
            error(str(e))
            return False