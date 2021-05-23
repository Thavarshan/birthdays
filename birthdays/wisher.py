import random
import json
from birthdays.emails import Email, BirthdayEmail
from birthdays.mailer import Mailer, SMTPMailer
from decouple import config
from pathlib import Path


class Wisher:
    fromaddr = None

    def __init__(self, mailer: Mailer, email: Email):
        self.mailer = mailer
        self.birthday_email = email
        self.__poem_file = Path('.') / 'data/poems.json'

    def wish_person(self, name, email):
        if self.fromaddr is None:
            raise RuntimeError('From address not set.')
        content = self.birthday_email.make_email(
            self.fromaddr, email, name, self.pick_random_poem()
        )
        self.mailer.send_mail(content)
        return name

    def pick_random_poem(self):
        with open(self.__poem_file, 'r+') as poems:
            return random.choice(json.load(poems))

    def set_from_address(self, email):
        self.fromaddr = email


def createWisher():
    wisher = Wisher(
        SMTPMailer({
            'email': config('MAIL_FROM_ADDRESS'),
            'password': config('GMAIL_PASSWORD')
        }),
        BirthdayEmail()
    )
    wisher.set_from_address(config('MAIL_FROM_ADDRESS'))
    return wisher
