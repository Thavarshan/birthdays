import smtplib
from pprint import pprint
from abc import ABC, abstractmethod
from birthdays.gmail import buildService
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail


class Mailer(ABC):
    credentials = None

    def __init__(self, credentials):
        self.credentials = credentials

    @abstractmethod
    def createService(self):
        pass

    @abstractmethod
    def send_mail(self, content):
        pass

    def set_credentials(self, email, password):
        self.credentials['email'] = email
        self.credentials['password'] = password


class SMTPMailer(Mailer):
    def createService(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(
                self.credentials['email'],
                self.credentials['password']
            )
            return smtp

    def send_mail(self, content):
        smtp = self.createService()
        smtp.sendmail(content)


class GoogleMailer(Mailer):
    def createService(self):
        return buildService()

    def send_mail(self, content):
        service = self.createService()
        service.users().messages().send(
            userId='me', body=content
        ).execute()


class SendgridMailer(Mailer):
    def createService(self):
        return sendgrid.SendGridAPIClient(
            apikey=config("SENDGRID_API_KEY")
        )

    def send_mail(self, content):
        pass
