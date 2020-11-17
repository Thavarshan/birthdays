import random
import json
from .emails import BirthdayEmail
from .mailer import OAuthMailer
from decouple import config
from pathlib import Path


class Wisher:

    def __init__(self):
        self.mailer = OAuthMailer()
        self.birthday_email = BirthdayEmail()
        self.__poem_file = Path('.') / 'data/poems.json'

    def wish_person(self, email):
        fromaddr = config('MAIL_FROM_ADDRESS')
        content = self.birthday_email.make_email(
            fromaddr, email, self.pick_random_poem()
        )
        self.mailer.send_mail(fromaddr, email, content)

    def pick_random_poem(self):
        with open(self.__poem_file, 'r+') as poems:
            return random.choice(json.load(poems))
