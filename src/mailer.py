import smtplib
from .config import Config


class Mailer:

    def __init__(self, config: Config):
        self.config = config

    def send_email(self, email: str, content: str):
        content['From'] = email
        content['To'] = self.config.gmail_email
        with smtplib.SMTP(self.config.host, self.config.port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.config.gmail_email, self.config.gmail_password)
            server.send_message(content)
