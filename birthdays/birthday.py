from decouple import config
from datetime import datetime
from pprint import pprint


class Birthday:
    __birthdays = []
    wisher = None

    def __init__(self, wisher):
        self.wisher = wisher

    def check_for_birthdays_today(self, people=[]):
        for person in people:
            if self.is_birthday_today(person.get('birthday')):
                self.wish_person(person)
                self.__birthdays.append(person.get('id'))
        return self.__birthdays

    def wish_person(self, person):
        return self.wisher.wish_person(person.get('name'), person.get('email'))

    def is_birthday_today(self, birthday):
        try:
            birthday = (
                datetime
                .strptime(birthday, '%Y-%m-%dT%H:%M:%S.%fZ')
                .strftime('%d-%m')
            )
        except ValueError:
            birthday = birthday[:5]
        finally:
            return bool(birthday == datetime.now().strftime('%d-%m'))

    def birthdays_today(self):
        return self.__birthdays
