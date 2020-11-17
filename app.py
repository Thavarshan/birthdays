from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from src.birthdays import Birthdays


def main(people: str):
    birthdays = Birthdays()
    birthdays.check_for_birthdays_today(people)


if __name__ == '__main__':
    main('data/people.json')
