import json
from .wisher import Wisher
from datetime import datetime


class Birthdays:

    def __init__(self):
        self.wisher = Wisher()

    def check_for_birthdays_today(self, people: str):
        with open(people, 'r+') as everyone:
            for person in json.load(everyone):
                if person.get('birthday')[:5] == datetime.now().strftime("%d-%m"):
                    self.wisher.wish_person(person.get('email'))
