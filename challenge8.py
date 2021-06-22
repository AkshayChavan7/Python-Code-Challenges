'''
Challenge 8: Sending an Email

Inputs: receiving email, Subject, body
'''

import smtplib

sender = 'akshay.chavan@finiq.com'
password = 'password'

receiver = 'akshay.chavan@finiq.com'
subject = 'Test Mail'
text = 'Hello world'
body = '\r\n'.join( [ 'To: %s' %receiver,
                      'From: %s' %sender,
                      'Subject: %s' %subject,
                      '', text
    ])


server = smtplib.SMTP('smtp.gmail.com',587)
#server.ehlo()
server.starttls()
server.login(sender, password)


try:
    server.sendmail(sender,[receiver], body)
    print('Email sent successfully!')
except SMTPException:
    print('Error: unable to sent Email')

server.quit()
