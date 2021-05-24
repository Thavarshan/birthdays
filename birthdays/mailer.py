import smtplib
import ssl
from abc import ABC, abstractmethod


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

        with smtplib.SMTP_SSL('smtp.gmail.com:465', context=context) as smtp:
            smtp.login(email, self.credentials.get('password'))
            smtp.sendmail(email, args.get('to'), args.get('message'))
