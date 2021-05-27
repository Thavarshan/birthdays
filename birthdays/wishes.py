import random
import json


class Wish:

    def __init__(self, wishes):
        self.wishes = wishes

    def create_wish(self):
        with open(self.wishes, 'r+') as wishes:
            return random.choice(json.load(wishes))
