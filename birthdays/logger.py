from datetime import datetime
from .requests import Requests


class Logger:

    def __init__(self):
        self.requests = Requests()

    def log(self, students):
        self.requests.post({
            "init_time": str(datetime.now()),
            "students": students,
            "status": True
        })

    def log_error(self, error):
        self.requests.post({
            "init_time": str(datetime.now()),
            "status": False,
            "context": error
        })
