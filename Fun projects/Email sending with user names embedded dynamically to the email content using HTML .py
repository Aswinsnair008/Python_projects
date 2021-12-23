import smtplib 
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=template(path(index.html).read_text(),'html')
email = EmailMessage()
email['from'] = 'User Name'
email['to'] = 'username@gmail.com' 
email['subject'] = 'this is just a test email sent to make sure that it works with python'
email.set_content(html.substitute(name = 'tintin'))
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('username@gmail.com' ,'app_specificpassword')
	smtp.send_message(email)
	print ('all good boss')
