import os
from abc import ABC
from dotenv import load_dotenv
from pathlib import Path


class Config(ABC):

    host = 'smtp.gmail.com'
    ssl_port = 465

    def __init__(self):
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)
        self.gmail_email = os.getenv('GMAIL_ID')
        self.gmail_password = os.getenv('GMAIL_PWD')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
