import json
from src.birthdays import Birthdays
from pathlib import Path


def main(people=None):
    birthdays = Birthdays()
    birthdays.check_for_birthdays_today(people)


if __name__ == '__main__':
    with open(Path('.') / 'tests/fixtures/people-test.json', 'r+') as people:
        main(json.load(people))
