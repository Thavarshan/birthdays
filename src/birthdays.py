import json
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
        token = config('API_TOKEN')
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(
            'http://batch-95.test/api/ping', headers=headers
        )
        [self.wish_person(person.get('email')) for person
         in response.json()
         if self.is_birthday_today(person.get('birthday'))]

    def wish_person(self, email):
        self.wisher.wish_person(email)

    def is_birthday_today(self, birthday):
        birthday = (
            datetime
            .strptime(birthday, '%Y-%m-%dT%H:%M:%S.%fZ')
            .strftime("%d-%m")
        )
        return birthday == datetime.now().strftime("%d-%m")
