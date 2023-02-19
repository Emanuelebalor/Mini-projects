from email.message import EmailMessage
import ssl
import smtplib

email_sender = ""  # Here goes your email
email_password = ""  # this is not your email password, you need to allow python to send mail from gmail
# and you'll get a 16 chars code that goes here
email_receiver = "lehiyi6998@iucake.com"  # temp email, this is where email receiver goes


subject = "This is a test"  # mail subject
# this is the body of the email
body = """  
This is the test
"""

# create an instance
inst = EmailMessage()
inst['From'] = email_sender
inst['To'] = email_receiver
inst['Subject'] = subject
inst.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, inst.as_string())

