import unittest
from birthdays.emails import BirthdayEmail


class BirthdayEmailTest(unittest.TestCase):

    content = [
        'Dear Thavarshan,',
        'Happy birthday!',
        'From your batch mates at ICBT.'
    ]

    def test_build_content(self):
        birthday_email = BirthdayEmail()
        email_content = birthday_email.build_content(
            'Thavarshan', 'Happy birthday!'
        ).splitlines()
        self.assertEqual(self.content, email_content)
