from decouple import config
import sys
from pprint import pprint
from birthdays import find_birthdays, create_email, create_wish, get_people, send_mail


def run():
    try:
        birthdays = find_birthdays(get_people())

        for birthday in birthdays:
            send_mail(create_email(
                config('MAIL_FROM_ADDRESS'),
                birthday.get('email'),
                birthday.get('name'),
                'Wish you a very happy birthday!',
                create_wish()
            ))

            pprint(birthday.get('name'))
    except:
        pprint(str(sys.exc_info()))


if __name__ == '__main__':
    run()
