import sys
from datetime import datetime
from pprint import pprint
from decouple import config
from birthdays.birthday import Birthday
from birthdays.wisher import createWisher
from birthdays.api import API


def main():
    api = API(config('API_TOKEN'))
    birthday = Birthday(createWisher())
    try:
        birthdays = birthday.check_for_birthdays_today(
            api.get(config('CONTACTS_URI')).json()
        )
        data = {
            'status': True,
            'context': 'Successful',
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
