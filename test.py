import json
from datetime import datetime


if __name__ == '__main__':
    today = datetime.now().strftime("%d-%m")
    with open('people.json', 'r+') as everyone:
        for person in json.load(everyone):
            print(person.get('birthday'))
