import smtplib
from email.mime.text import MIMEText

MessageBody = "This should be passed as an arg"
SMTP_SERVER = "mail.example.com"
SMTP_USER = "user@example.com"
SMTP_PSWD = "p@s5w0rd1!"

message = MIMEText(MessageBody)
message['Subject'] = "Subject String"
message['From'] = "From@Email.Com"
message['To'] = "To@Email.com"

s = smtplib.SMTP(SMTP_SERVER)

if (auth_required):
    s.login(SMTP_USER, SMTP_PSWD)

s.sendmail(message['From'], [message['To']], message.as_string())
