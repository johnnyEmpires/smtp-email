import os
import smtplib
import ssl
import cred
from email.message import EmailMessage
import time


port = 465 # SSL
smtp_server = 'smtp.gmail.com'
sender_email = cred.user
password = cred.pwd

# email
msg = EmailMessage()

systime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
msg['Subject'] = f'System notification update [{systime} GMT]'


# receivers
with open('mail_list') as ml:
	"""
	create a `mail_list` file and add contents like below

	email1@domain.com
	second_email@domain.com
	
	and so on ...

	"""

	rcvr = ml.readlines()
	rcvr = [x.replace('\n', '') for x in rcvr]

ctx = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=ctx) as server:
	try:
		server.ehlo()
		server.login(sender_email, password)

		msg.set_content(f'system generated message')
		server.sendmail(sender_email, rcvr, msg.as_string())

	except Exception as e:
		print('an error occurred during email send process')
		print(str(e))
