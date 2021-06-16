import smtplib
import ssl
from abc import ABC, abstractmethod
from decouple import config
from sendgrid import SendGridAPIClient


class Mailer(ABC):

    credentials = None

    def __init__(self, credentials):
        self.credentials = credentials

    @abstractmethod
    def send_mail(self, **args):
        pass


class SMTPMailer(Mailer):

    def send_mail(self, **args):
        email = self.credentials.get('email')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config('MAIL_HOST'), config('MAIL_PORT'), context=context) as smtp:
            smtp.login(email, self.credentials.get('password'))
            smtp.sendmail(email, args.get('to'), args.get('message'))


class SendgridMailer(Mailer):

    def send_mail(self, **args):
        sendgrid = SendGridAPIClient(self.credentials.get('api_key'))
        sendgrid.send(args.get('message'))
