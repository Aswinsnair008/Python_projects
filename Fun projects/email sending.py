import smtplib 
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'username'
email['to'] = 'username@gmail.com'  
email['subject'] = 'this is just a test email sent to make sure that it works with python'
email.set_content('here we will be adding the content that we will sent as email, we can use text,html,images')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('username@gmail.com','app_specificpassword')
	smtp.send_message(email)
	print ('all good boss')
