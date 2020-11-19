from .wisher import Wisher
from datetime import datetime
from .emails import BirthdayEmail
from .mailer import OAuthMailer
import requests
from decouple import config


class Birthdays:

    def __init__(self):
        self.wisher = Wisher(OAuthMailer(), BirthdayEmail())

    def check_for_birthdays_today(self, people=None):
        if people == None:
            people = self.get_data(
                config('API_ENDPOINT'), config('API_TOKEN')
            ).json()
        self.find_birthdays_and_mail_wishes(people)

    def find_birthdays_and_mail_wishes(self, people):
        [self.wish_person(person) for person
            in people if self.is_birthday_today(person.get('birthday'))]

    def get_data(self, endpoint, token):
        return requests.get(endpoint, headers={'Authorization': f'Bearer {token}'})

    def wish_person(self, person):
        self.wisher.wish_person(person.get('name'), person.get('email'))

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
