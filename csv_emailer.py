import time
import schedule
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64
from csv import reader
import re

data = open('logo_for_top_of_email.png', 'rb').read()  # read bytes from file
data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
data_base64 = data_base64.decode()  # convert bytes to string


def email(html, login, email):
    msg = MIMEMultipart('alternative')

    msg['Subject'] = 'Email Subject Example'
    msg['From'] = "from@email.com"
    msg['To'] = email
    #set as html
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.server.com', 465)
    server.login("example@email.com", "password")
    server.send_message(msg)
    server.quit()


with open('csv_example.csv', 'r') as csv:
    csv_reader = reader(csv)
    header = next(csv_reader)
    if header != None:
        for row in csv_reader:
            login = row[2]
            dealerEmail = row[3]

            html = '<html lang="en"><head><meta charset="utf-8"><title>Your In The Ditch™.com Account Information</title><meta name="description" content="The HTML5 Herald"><meta name="author" content="In The Ditch™"></head><body style="background-color:#f2f2f2; margin:0px; padding:0px; font-family:arial; font-size:12px;"><table style="width:100%; max-width:650px; height:100%; background-color:#fff; margin:auto; padding:0px;"><tr><td><table style="width:100%; text-align:center;"><tr style="width:inherit; height:4px; background-color:#0076c0"></tr><tr style="width:inherit;"><td style="padding:15px;"><img src="data:image/jpeg;base64,' + data_base64 + '"/></td></tr></table></td></tr><tr style="width:100%;"><td style="width:100%;"><table style="width:100%; padding:25px;"><tr><h3>Your In The Ditch™.com Account Information</h3></tr><tr style="margin-bottom: 20px;"><p>You\'ve already been signed up for an account on our new website! To set your own password, follow this link and use the provided username or email address to receive a password reset email.</p></tr><tr><h3>User Name: ' + login + '</tr><h3>To reach our password reset page, Follow This Link: </h3><a href="https://intheditch.com/my-account/lost-password/">https://intheditch.com</a></tr></table></td></tr><tr><td><table style="width:100%; text-align:center; background-color:#262626;"><tr style="width:inherit;"><td style="padding:15px;"></td></tr><tr style="width:inherit;"><td style="text-align:center; color:#fff; width:100%; padding:15px;"><p style="line-height:1.5;"><strong>In The Ditch&#8482; Towing Products</strong><br />3190 Industrial Way, Mountain Home, ID 83647<br />Phone: <a style="text-decoration:none; color:#fff;" href="tel:12085877960">1 (208) 587-7960</a><br />Email: <a style="text-decoration:none; color:#fff;" href="mailto:sales@intheditch.com">sales@intheditch.com</a><br/><a style="text-decoration:none; color:#fff;"href="https://intheditch.com"> intheditch.com</a></p></td></tr></table></td></tr><tr style="width:inherit;"><td style="text-align:center; color:#d9d9d9; width:100%;"><p>Copyright - In The Ditch&trade; Towing Products</p></td></tr></table></body></html>'

            email(html, login, dealerEmail)
            print('Email Sent to: {}'.format(dealerEmail))