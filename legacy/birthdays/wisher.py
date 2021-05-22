import random
import json
from .emails import Email
from .mailer import Mailer
from decouple import config
from pathlib import Path


class Wisher:
    def __init__(self, mailer: Mailer, email: Email):
        self.mailer = mailer
        self.birthday_email = email
        self.__poem_file = Path('.') / 'data/poems.json'
        self.fromaddr = config('MAIL_FROM_ADDRESS')

    def wish_person(self, name, email):
        content = self.birthday_email.make_email(
            self.fromaddr, email, name, self.pick_random_poem()
        )
        if config('APP_ENV') == 'production':
            self.mailer.send_mail(self.fromaddr, email, content)
        return name

    def pick_random_poem(self):
        with open(self.__poem_file, 'r+') as poems:
            return random.choice(json.load(poems))
