import requests
from datetime import datetime
from birthdays.emails import SendgridBirthdayEmail
from pathlib import Path
from birthdays.wishes import Wish
from birthdays.mailer import SendgridMailer
from birthdays.birthdays import Birthday
from decouple import config


def get_people():
    response = requests.get(config('CONTACTS_URI'), headers={
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + config('API_TOKEN'),
        'Content-Type': 'application/json',
    })

    return response.json()


def find_birthdays(people):
    birthday = Birthday(people)

    return birthday.find_birthdays()


def create_wish():
    wisher = Wish(Path('.') / 'data/wishes.json')

    return wisher.create_wish()


def create_email(fromaddr, fromname, toaddr, toname, subject, content):
    email = SendgridBirthdayEmail()

    return email.make_email(fromaddr, fromname, toaddr, name, subject, content)


def send_mail(email, message):
    mailer = SendgridMailer({
        'api_key': config('SENDGRID_API_KEY'),
    })

    mailer.send_mail(message=message)
