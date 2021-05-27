from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import lxml.html
from sendgrid.helpers.mail import To, Email as SendgridEmail, Mail


class Email(ABC):

    def build_content(self, name, content):
        return f"Dear {name},\n\n" + content + "\n"

    @abstractmethod
    def make_email(self, fromaddr, fromname, toaddr, toname, subject, content):
        pass


class BirthdayEmail(Email):

    def make_email(self, fromaddr, fromname, toaddr, toname, subject, content):
        content = self.build_content(toname, content)
        message = MIMEMultipart('related')
        message['From'] = fromaddr
        message['To'] = toaddr
        message['Subject'] = subject
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


class SendgridBirthdayEmail(Email):

    def make_email(self, fromaddr, fromname, toaddr, toname, subject, content):
        return Mail(
            SendgridEmail(email=fromaddr, name=fromname),
            To(email=toaddr, name=toname),
            subject,
            self.build_content(toname, content)
        )
