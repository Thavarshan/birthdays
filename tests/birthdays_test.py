
import json
import unittest
from datetime import datetime
from birthdays.birthdays import Birthdays


class BirthdaysTest(unittest.TestCase):

    def test_is_birthday_today_accepts_date_as_string(self):
        birthday = Birthdays()
        self.assertTrue(
            birthday.is_birthday_today(datetime.now().strftime("%d-%m"))
        )

    def test_is_birthday_today_accepts_date_as_iso_standard_format_string(self):
        birthday = Birthdays()
        self.assertTrue(birthday.is_birthday_today(
            datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        ))

    def test_wishes_person_with_birthday_today(self):
        birthday = Birthdays()
        self.assertEqual('James', birthday.wish_person({
            "name": "James",
            "email": 'james@example.com'
        }))

    def test_logs_person_details_after_wishing(self):
        birthday = Birthdays()
        birthday.wish_person({
            "name": "James",
            "email": 'james@example.com'
        })
        self.assertEqual('James', birthday.birthdays_today()[0])

    def test_checks_for_peopls_birthdays_and_wishes_them(self):
        birthday = Birthdays()
        birthday.check_for_birthdays_today([
            {
                "name": "James",
                "email": 'james@example.com',
                "birthday": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        ])
        self.assertEqual('James', birthday.birthdays_today()[0])
