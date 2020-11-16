import re
import smtpd
import threading
import asyncore


class MockSMTPServer(smtpd.SMTPServer, threading.Thread):
    '''
    A mock SMTP server. Runs in a separate thread so can be started from
    existing test code.
    '''

    def __init__(self, hostname, port):
        threading.Thread.__init__(self)
        smtpd.SMTPServer.__init__(self, (hostname, port), None)
        self.daemon = True
        self.received_messages = []
        self.start()

    def run(self):
        asyncore.loop()

    def process_message(self, peer, mailfrom, rcpttos, data):
        self.received_messages.append(data)

    def reset(self):
        self.received_messages = []

    # helper methods for assertions in test cases
    def received_message_matching(self, template):
        for message in self.received_messages:
            if re.match(template, message):
                return True
        return False

    def received_messages_count(self):
        return len(self.received_messages)
