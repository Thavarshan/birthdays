from .exceptions import MailNotSentException
import smtplib
from abc import ABC, abstractmethod
import base64
from decouple import config
import json
import urllib.parse
import urllib.request


class Mailer(ABC):

    @abstractmethod
    def send_mail(self, fromaddr, toaddr, content):
        pass


class SMTPMailer(Mailer):

    def send_mail(self, fromaddr, toaddr, content):
        with smtplib.SMTP_SSL(config('MAIL_SERVER'), config('MAIL_PORT')) as server:
            server.login(config('MAIL_FROM_ADDRESS'), config('MAIL_PASSWORD'))
            server.send_message(content)


class OAuthMailer(Mailer):

    def send_mail(self, fromaddr, toaddr, content):
        access_token, expires_in = self.refresh_authorization(config(
            'GOOGLE_CLIENT_ID'), config('GOOGLE_CLIENT_SECRET'), config('GOOGLE_REFRESH_TOKEN')
        )
        auth_string = self.generate_oauth2_string(
            fromaddr, access_token, as_base64=True
        )

        with smtplib.SMTP('smtp.gmail.com:587') as server:
            server.ehlo(config('GOOGLE_CLIENT_ID'))
            server.starttls()
            server.docmd('AUTH', 'XOAUTH2 ' + auth_string)
            server.sendmail(fromaddr, toaddr, content)
            if server.noop() is not (250, 'Ok'):
                raise MailNotSentException()

    def refresh_authorization(self, google_client_id, google_client_secret, refresh_token):
        response = self.call_refresh_token(
            google_client_id, google_client_secret, refresh_token
        )
        return response['access_token'], response['expires_in']

    def call_refresh_token(self, client_id, client_secret, refresh_token):
        params = {}
        params['client_id'] = client_id
        params['client_secret'] = client_secret
        params['refresh_token'] = refresh_token
        params['grant_type'] = 'refresh_token'
        request_url = self.command_to_url('o/oauth2/token')
        response = urllib.request.urlopen(
            request_url, urllib.parse.urlencode(params).encode('UTF-8')
        ).read().decode('UTF-8')
        return json.loads(response)

    def command_to_url(self, command):
        return '%s/%s' % (config('GOOGLE_ACCOUNTS_BASE_URL'), command)

    def generate_oauth2_string(self, username, access_token, as_base64=False):
        auth_string = 'user=%s\1auth=Bearer %s\1\1' % (username, access_token)
        if as_base64:
            auth_string = base64.b64encode(
                auth_string.encode('ascii')
            ).decode('ascii')
        return auth_string
