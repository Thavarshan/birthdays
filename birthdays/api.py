import requests


class API:
    __token = None

    def __init__(self, token):
        self.__token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.__token}',
        }

    def get(self, uri):
        return requests.get(uri, headers=self.get_headers())

    def post(self, uri, data={}):
        return requests.post(uri, json=data, headers=self.get_headers())
