import sys
from decouple import config
import json
from src.logger import Logger
from src.birthdays import Birthdays
from pathlib import Path


def main(people=None):
    try:
        birthdays = Birthdays()
        birthdays.check_for_birthdays_today(people)
    except:
        logger = Logger()
        logger.log_error(str(sys.exc_info()[0]))


if __name__ == '__main__':
    if config('APP_ENV') == 'local':
        with open(Path('.') / 'tests/fixtures/people-test.json', 'r+') as people:
            main(json.load(people))
    else:
        main()
