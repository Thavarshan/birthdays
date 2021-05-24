import datetime


class Birthday:

    __birthdays = []

    def __init__(self, people=[]):
        self.people = people

    def find_birthdays(self):
        for person in self.people:
            if self.is_birthday_today(person.get('birthday')):
                self.__birthdays.append(person)

        return self.__birthdays

    def is_birthday_today(self, birthday):
        birthday = (
            datetime
            .strptime(birthday, '%Y-%m-%dT%H:%M:%S.%fZ')
            .strftime('%d-%m')
        )

        return bool(birthday == datetime.now().strftime('%d-%m'))
