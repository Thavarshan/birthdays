from birthdays.birthday import Birthday
import sys
from birthdays.wisher import createWisher
from datetime import datetime
from pprint import pprint
from birthdays.api import API
from decouple import config


def main():
    api = API(config('API_TOKEN'))
    birthday = Birthday(createWisher())
    try:
        birthdays = birthday.check_for_birthdays_today(
            api.get(config('CONTACTS_URI')).json()
        )
        data = {
            'status': True,
            'context': '',
            'contacts': birthdays
        }
    except:
        data = {
            'status': False,
            'context': str(sys.exc_info()),
            'contacts': []
        }
    response = api.post(config('LOGGING_URI'), data={
        **data,
        'app_name': config('APP_NAME'),
        'init_time': str(datetime.now()),
    })
    pprint(response.text)


if __name__ == '__main__':
    main()
