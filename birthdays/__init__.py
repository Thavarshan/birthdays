import requests
from birthdays.emails import BirthdayEmail
from pathlib import Path
from birthdays.wishes import Wish
from birthdays.mailer import SMTPMailer
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
    email = BirthdayEmail()
    return email.make_email(fromaddr, fromname, toaddr, toname, subject, content)


def send_mail(email, message):
    mailer = SMTPMailer({
        'email': config('MAIL_FROM_ADDRESS'),
        'password': config('MAIL_PASSWORD')
    })
    mailer.send_mail(to=email, message=message)
