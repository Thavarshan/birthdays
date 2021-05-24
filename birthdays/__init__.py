from birthdays.mailer import SMTPMailer
from birthdays.birthdays import Birthday


def find_birthdays(people):
    birthday = Birthday(people)
    return birthday.find_birthdays()


def send_mail(email, message):
    mailer = SMTPMailer({
        'email': 'example@mail.com',
        'password': 'password123'
    })
    mailer.send_mail(to=email, message=message)
