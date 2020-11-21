from .wisher import Wisher
from .logger import Logger
from datetime import datetime
from .emails import BirthdayEmail
from .mailer import OAuthMailer
import requests
from decouple import config


class Birthdays:

    __birthdays = []

    def __init__(self):
        self.wisher = Wisher(OAuthMailer(), BirthdayEmail())
        self.logger = Logger()
        self.__api_token = config('API_TOKEN')

    def check_for_birthdays_today(self, people=None):
        if people == None:
            people = self.get_data(config('API_ENDPOINT')).json()
        self.find_birthdays_and_mail_wishes(people)
        self.logger.log(self.__birthdays)

    def find_birthdays_and_mail_wishes(self, people):
        [self.wish_person(person) for person
            in people if self.is_birthday_today(person.get('birthday'))]

    def get_data(self, endpoint):
        return requests.get(
            endpoint, headers={
                'Authorization': f'Bearer {self.__api_token}',
                'X-App-Name': config('APP_NAME')
            }
        )

    def wish_person(self, person):
        self.wisher.wish_person(person.get('name'), person.get('email'))
        self.__birthdays.append(person.get('name'))

    def is_birthday_today(self, birthday):
        try:
            birthday = (
                datetime
                .strptime(birthday, '%Y-%m-%dT%H:%M:%S.%fZ')
                .strftime("%d-%m")
            )
        except ValueError:
            birthday = birthday[:5]
        finally:
            return bool(birthday == datetime.now().strftime("%d-%m"))
