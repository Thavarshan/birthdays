import json
import unittest
from birthdays.wisher import Wisher
from birthdays.mailer import OAuthMailer
from birthdays.mailer import Mailer
from birthdays.emails import BirthdayEmail


class WisherTest(unittest.TestCase):

    def setUp(self):
        self.wisher = Wisher(OAuthMailer(), BirthdayEmail())

    def test_pick_random_poem(self):
        with open('data/poems.json', 'r+') as poem_file:
            poems = json.load(poem_file)

        self.assertIs(type(self.wisher.pick_random_poem()), str)
        self.assertTrue(self.wisher.pick_random_poem() in poems)

    def test_has_instance_of_mailer(self):
        self.assertIsInstance(self.wisher.mailer, Mailer)

    def test_has_instance_of_email_maker(self):
        self.assertIsInstance(self.wisher.birthday_email, BirthdayEmail)

    def test_wish_person(self):
        self.assertEqual('James', self.wisher.wish_person(
            'James',
            'james@example.com'
        ))
