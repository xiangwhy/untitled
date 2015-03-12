import smtplib

sender = '240451@qq.com'
receivers = ['240451@qq.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except:
    print("Error: unable to send email")