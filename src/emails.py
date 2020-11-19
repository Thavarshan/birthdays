from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import lxml.html


class Email(ABC):

    @abstractmethod
    def make_email(self, content):
        pass


class BirthdayEmail(Email):

    def build_content(self, name, content):
        return f"Dear {name}\n," + content + "\nFrom your batch mates at ICBT."

    def make_email(self, fromaddr, toaddr, name, content):
        content = self.build_content(name, content)
        message = MIMEMultipart('related')
        message['From'] = fromaddr
        message['To'] = toaddr
        message['Subject'] = f'Wish you a very happy birthday!'
        message.preamble = 'This is a multi-part message in MIME format.'
        message_alternative = MIMEMultipart('alternative')
        message.attach(message_alternative)
        part_text = MIMEText(
            lxml.html.fromstring(content).text_content().encode('utf-8'),
            'plain',
            _charset='utf-8'
        )
        part_html = MIMEText(content.encode('utf-8'), 'html', _charset='utf-8')
        message_alternative.attach(part_text)
        message_alternative.attach(part_html)
        return message.as_string()
