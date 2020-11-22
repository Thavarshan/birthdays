from datetime import datetime
from .requests import Requests


class Logger:

    def __init__(self):
        self.requests = Requests()

    def log(self, students):
        return self.requests.post(data={
            "init_time": str(datetime.now()),
            "students": students,
            "status": True,
            "context": None
        })

    def log_error(self, error):
        return self.requests.post(data={
            "init_time": str(datetime.now()),
            "students": {},
            "status": False,
            "context": error
        })
