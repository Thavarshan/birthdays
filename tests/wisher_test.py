import json
import unittest
from src.wisher import Wisher
from src.mailer import Mailer
from src.emails import BirthdayEmail
from .mock_smtp import MockSMTPServer


class WisherTest(unittest.TestCase):

    def test_pick_random_poem(self):
        wisher = Wisher()
        with open('poems.json', 'r+') as poem_file:
            poems = json.load(poem_file)

        self.assertIs(type(wisher.pick_random_poem()), str)
        self.assertTrue(wisher.pick_random_poem() in poems)

    def test_has_instance_of_mailer(self):
        wisher = Wisher()
        self.assertIsInstance(wisher.mailer, Mailer)

    def test_has_instance_of_email_maker(self):
        wisher = Wisher()
        self.assertIsInstance(wisher.birthday_email, BirthdayEmail)

    def test_wish_person(self):
        wisher = Wisher()
        wisher.wish_person('tjthavarshan@gmail.com')
        mock_server = MockSMTPServer()
        self.assertTrue(1, mock_server.received_messages_count())
