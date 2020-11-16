import smtplib
import ssl
from .config import Config


class Mailer:

    def __init__(self, config: Config):
        self.config = config

    def send_email(self, email: str, content: str):
        content['From'] = email
        content['To'] = self.config.gmail_email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.config.host, self.config.ssl_port, context=context) as server:
            server.login(self.config.gmail_email, self.config.gmail_password)
            server.send_message(content)
