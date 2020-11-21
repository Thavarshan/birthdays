from datetime import datetime
import requests
from decouple import config


class Logger:

    def __init__(self):
        self.__endpoint = config('API_LOGGING_ENDPOINT')
        self.__api_token = config('API_TOKEN')
        self.__app_name = config('APP_NAME')

    def log(self, students):
        response = requests.post(
            self.__endpoint,
            json={
                "init_time": str(datetime.now()),
                "students": students,
                "status": True
            },
            headers={
                'Authorization': f'Bearer {self.__api_token}',
                'X-App-Name': self.__app_name
            }
        )

    def log_error(self, error):
        requests.post(
            self.__endpoint,
            json={
                "init_time": str(datetime.now()),
                "status": False,
                "context": error
            },
            headers={
                'Authorization': f'Bearer {self.__api_token}',
                'X-App-Name': self.__app_name
            }
        )
