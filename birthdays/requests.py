import requests
from decouple import config


class Requests:

    def __init__(self):
        self.__post_endpoint = config('API_LOGGING_ENDPOINT')
        self.__get_endpoint = config('API_ENDPOINT')
        self.__api_token = config('API_TOKEN')
        self.__app_name = config('APP_NAME')

    def get(self, endpoint=None):
        if endpoint == None:
            endpoint = self.__get_endpoint
        return requests.get(endpoint, headers={
            'Authorization': f'Bearer {self.__api_token}',
            'X-App-Name': self.__app_name
        })

    def post(self, endpoint, data={}):
        if endpoint == None:
            endpoint = self.__post_endpoint
        return requests.post(self.__post_endpoint, json=data, headers={
            'Authorization': f'Bearer {self.__api_token}',
            'X-App-Name': self.__app_name
        })
