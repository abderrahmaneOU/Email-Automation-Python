# send_email.py
# Sends an email using Gmail credentials from environment variables
import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_sender = os.getenv('GMAIL_USER')
email_password = os.getenv('GMAIL_PASSWORD')
email_receiver = os.getenv('RECIPIENT_EMAIL')

subject = 'check my email'
body = """
I've just finished school and I'm looking for money. Work for me or you'll get banned from the hoho company. That's all.
"""

if not email_sender or not email_password or not email_receiver:
    raise ValueError("GMAIL_USER, GMAIL_PASSWORD, or RECIPIENT_EMAIL is not set. Please check your .env file.")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
