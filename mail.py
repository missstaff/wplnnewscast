from email.mime.text import MIMEText
import os
import smtplib

def send_email(body):
    sender = "audiobatonmusic@gmail.com"
    recipients = ["fertilityhollis88@gmail.com"]
    password = os.environ['email_pass']
    
    msg = MIMEText(body)
    msg['Subject'] = "WPLN Newscast Comment"
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()