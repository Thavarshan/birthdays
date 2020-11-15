from dotenv import load_dotenv
from datetime import datetime
import smtplib
import os
import json
from message import CONTENT
import logging
from email.message import EmailMessage


def main(people: str):
    load_dotenv()
    with open(people, 'r+') as everyone:
        for person in json.load(everyone):
            if person.get('birthday') == datetime.now().strftime("%d-%m"):
                wish_person(person.get('email'))


def wish_person(email: str):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(os.getenv("GMAIL_ID"), os.getenv("GMAIL_PWD"))
            server.sendmail(os.getenv("GMAIL_ID"), email, CONTENT)
    except Exception as e:
        logging.error(str(e))


if __name__ == '__main__':
    main('people.json')
