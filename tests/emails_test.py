import unittest
from src.emails import BirthdayEmail


class BirthdayEmailTest(unittest.TestCase):

    def test_build_content(self):
        birthday_email = BirthdayEmail()
        print(birthday_email.build_content('Thavarshan', 'Happy birthday!'))
