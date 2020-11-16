import random
import json
from .emails import BirthdayEmail
from .mailer import Mailer
from .config import ProductionConfig


class Wisher:

    __poem_file = 'poems.json'

    def __init__(self):
        self.mailer = Mailer(ProductionConfig())
        self.birthday_email = BirthdayEmail()

    def wish_person(self, email: str):
        content = self.birthday_email.make_email(self.pick_random_poem())
        self.mailer.send_email(email, content)

    def pick_random_poem(self):
        with open(self.__poem_file, 'r+') as poems:
            return random.choice(json.load(poems))
