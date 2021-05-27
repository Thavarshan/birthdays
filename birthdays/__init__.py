import requests
from birthdays.emails import BirthdayEmail
from pathlib import Path
from birthdays.wishes import Wish
from birthdays.mailer import SendgridMailer
from birthdays.birthdays import Birthday
from decouple import config


def get_people():
    response = requests.get(config('CONTACTS_URI'), headers={
        'Authorization': 'Bearer ' + config('API_TOKEN'),
    })

    return response.json()


def find_birthdays(people):
    birthday = Birthday(people)

    return birthday.find_birthdays()


def create_wish():
    wisher = Wish(Path('.') / 'data/wishes.json')

    return wisher.create_wish()


def create_email(fromaddr, toaddr, name, subject, content):
    email = BirthdayEmail()

    return email.make_email(fromaddr, toaddr, name, subject, content)


def send_mail(email, message):
    mailer = SendgridMailer({
        'api_key': config('SENDGRID_API_KEY'),
    })

    mailer.send_mail(message=message)
