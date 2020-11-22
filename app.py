import sys
from decouple import config
import json
from birthdays.logger import Logger
from birthdays.birthdays import Birthdays


def main(people=None):
    try:
        birthdays = Birthdays()
        birthdays.check_for_birthdays_today(people)
    except:
        logger = Logger()
        logger.log_error(str(sys.exc_info()[0]))


if __name__ == '__main__':
    if config('APP_ENV') == 'local':
        with open('tests/fixtures/people-test.json', 'r+') as people:
            main(json.load(people))
    else:
        main()
