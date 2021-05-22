from pprint import pprint
from abc import ABC, abstractmethod
from googleapiclient.discovery import build


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


class SMTPMailer(Mailer):
    def createService(self):
        pass

    @abstractmethod
    def send_mail(self, content):
        pass


class OAuthMailer(Mailer):
    def createService(self):
        return build('gmail', 'v1', credentials=self.credentials)

    def send_mail(self, content):
        pprint(content)
        # service = self.createService()
        # service.users().messages().send(
        #     userId='me', body=content
        # ).execute()
