from abc import ABC, abstractmethod
from email.message import EmailMessage


class Email(ABC):

    @abstractmethod
    def make_email(self, content: str):
        pass


class BirthdayEmail(Email):

    def make_email(self, content: str):
        message = EmailMessage()
        message.set_content(content)
        message['Subject'] = f'Wish you a very happy birthday!'

        return message
