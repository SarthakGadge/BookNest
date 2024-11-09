from email.message import EmailMessage
import smtplib
import random
from django.utils import timezone
from django.db import connection
from django.conf import settings
import os
from dotenv import load_dotenv


def send_email(user):

    load_dotenv()

    otp = str(random.randint(1000, 9999))

    user.otp = otp
    user.otp_expiry = timezone.now() + timezone.timedelta(minutes=10)
    user.max_otp_try -= 1
    if user.max_otp_try == 0:
        user.otp_max_out = timezone.now() + timezone.timedelta(hours=1)
    user.save()

    email_to = user.email
    email_from = 'sarthakgadge43@gmail.com'
    email_password = os.getenv('password')

    subject = 'Verification of BookNest Account'

    # Email content in HTML format
    body = f'''
    <html>
    <body>
        <h2 style="color: #4A90E2;">Verify Your Email</h2>
        <p>Dear {user.username},</p>
        <p>You have registered a new account. Please use the following One-Time Password (OTP) to verify your email:</p>
        <p style="font-weight: bold; font-size: 18px;">OTP: <span style="color: #4A90E2;">{otp}</span></p>
        <p style="color: #777;">Note: Do not share this OTP with anyone. If you did not register this account, please ignore this email.</p>
        <p>Thank you,<br/>
        BookNest</p>
    </body>
    </html>
    '''

    # Set up the email
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = email_to
    em['Subject'] = subject
    em.set_content("This email requires HTML support to view the OTP.")
    em.add_alternative(body, subtype='html')  # Set HTML content

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        # Set up the SMTP server and start TLS
        with smtplib.SMTP(smtp_server, port) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(email_from, email_password)
            smtp.send_message(em)  # Send the email
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def forgot_password_email(user):

    load_dotenv()

    otp = str(random.randint(1000, 9999))

    user.otp = otp
    user.otp_expiry = timezone.now() + timezone.timedelta(minutes=10)
    user.max_otp_try -= 1
    if user.max_otp_try == 0:
        user.otp_max_out = timezone.now() + timezone.timedelta(hours=1)
    user.save()

    email_to = user.email
    email_from = 'sarthakgadge43@gmail.com'
    email_password = os.getenv('password')

    subject = 'Verification of BookNest Account'

    # Email content in HTML format
    body = f'''
    <html>
    <body>
        <h2 style="color: #4A90E2;">Resetting Your Password</h2>
        <p>Dear {user.username},</p>
        <p>Please use the following One-Time Password (OTP) to reset your password:</p>
        <p style="font-weight: bold; font-size: 18px;">OTP: <span style="color: #4A90E2;">{otp}</span></p>
        <p style="color: #777;">Note: Do not share this OTP with anyone. If you did not generate the otp, please ignore this email.</p>
        <p>Thank you,<br/>
        BookNest</p>
    </body>
    </html>
    '''

    # Set up the email
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = email_to
    em['Subject'] = subject
    em.set_content("This email requires HTML support to view the OTP.")
    em.add_alternative(body, subtype='html')  # Set HTML content

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        # Set up the SMTP server and start TLS
        with smtplib.SMTP(smtp_server, port) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(email_from, email_password)
            smtp.send_message(em)  # Send the email
            print("Email sent successfully!")
            return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
