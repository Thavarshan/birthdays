import json
from .wisher import Wisher
from datetime import datetime
from .emails import BirthdayEmail
from .mailer import OAuthMailer


class Birthdays:

    def __init__(self):
        self.wisher = Wisher(OAuthMailer(), BirthdayEmail())

    def check_for_birthdays_today(self, people):
        with open(people, 'r+') as everyone:
            [self.wish_person(person.get('email')) for person
                in json.load(everyone)
                if self.is_birthday_today(person.get('birthday'))]

    def wish_person(self, email):
        self.wisher.wish_person(email)

    def is_birthday_today(self, birthday):
        return birthday[:5] == datetime.now().strftime("%d-%m")
