import subprocess
import re
import os
import sys
import email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import OrderedDict
from email.mime.base import MIMEBase
from email import encoders


def email_generation(val, file_location, subject_conf, sender_email_conf, receiver_email_conf):
    print(receiver_email_conf)
    # Subject Line of the email
    subject = subject_conf
    sender_email = sender_email_conf
    receiver_email = receiver_email_conf
    # Create a multipart message and set headers
    message = MIMEMultipart('alternative')
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    msg = val
    body = MIMEText(msg, 'html')
    message.attach(body)
    file_name = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment;filename=%s " % file_name)
    message.attach(part)

    smtp = smtplib.SMTP('127.0.0.1', 7180)
    smtp.sendmail(sender_email, receiver_email.split(","), message.as_string())
    smtp.close()


email_generation("ok .. generate new mail", "LogFileNmae", "testing", "g.bhargav007@yahoo.com",
                 "g.bhargav007@yahoo.com")

