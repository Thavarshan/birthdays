from src.birthdays import Birthdays


def main(people=None):
    birthdays = Birthdays()
    birthdays.check_for_birthdays_today(people)


if __name__ == '__main__':
    main()
