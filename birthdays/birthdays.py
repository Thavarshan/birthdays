class Birthday:

    __birthdays = []

    def __init__(self, people=[]):
        self.people = people

    def find_birthdays(self):
        for person in self.people:
            if self.is_birthday_today(person):
                self.__birthdays.append(person)

        return self.__birthdays

    def is_birthday_today(self, person):
        pass
