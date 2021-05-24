import smtplib
from email.mime.text import MIMEText


password = 'zhmxkmfpxyjkohcu'
email = 'tjthavarshan@gmail.com'
message = MIMEText("It actually works!")
message['Subject'] = "Python Test Email"


def send_mail():
    with smtplib.SMTP_SSL('smtp.gmail.com:465') as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    send_mail()
