from .requests import Requests
from .wisher import Wisher
from .logger import Logger
from datetime import datetime
from .emails import BirthdayEmail
from .mailer import OAuthMailer
from decouple import config


class Birthdays:

    __birthdays = []

    def __init__(self):
        self.wisher = Wisher(OAuthMailer(), BirthdayEmail())
        self.logger = Logger()
        self.request = Requests()

    def check_for_birthdays_today(self, people=None):
        if people == None:
            people = self.requests.get().json()
        self.find_birthdays_and_mail_wishes(people)
        print(self.logger.log(self.__birthdays))

    def find_birthdays_and_mail_wishes(self, people):
        [self.wish_person(person) for person
            in people if self.is_birthday_today(person.get('birthday'))]

    def wish_person(self, person):
        self.__birthdays.append(person.get('name'))
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
