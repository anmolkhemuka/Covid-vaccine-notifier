#!/usr/bin/env python3
import urllib.request
import threading
import smtplib
import ssl
import requests
import json
import os
from twilio.rest import Client

# sender = input("Type the email that you would like to send emails FROM, and press enter: ")
# password = input("Type the password for that email and press enter: ")
# receiver = input("Type the email that you would like to send emails TO, and press enter: ")
sender = ""    
receiver =""
password = ""
counter=0
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
# How often to refresh the page, in seconds
UPDATE = 60.0 

# Port for SSL
port = 465  

# Message in the email.
text = "I am checking brother. Stay calm and safe"
subject = "check in progress"
message = 'Subject: {}\n\n{}'.format(subject, text)
# Create a secure SSL context
context = ssl.create_default_context()

# This function repeatedly reads the CVS website, and if any appointments are
# available in your state, it emails you.
def sendit():
  
    # Initializes threading (repition / refreshing of website)
    global counter
    #print(counter)
    threading.Timer(UPDATE, sendit).start()
    if(counter%120==0):
        counter=0
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
    counter = counter+1
    # Reads website into var 'html'
    req = urllib.request.Request('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=480661&date=09-05-2021',headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'})
    html= urllib.request.urlopen(req).read()
    a = json.loads(html)

    for p in  a['centers']:
        for s in p['sessions']:
            if  s['min_age_limit'] ==18 and s['available_capacity']>0 :
                print(p['name'])
                call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                         to='',
                        from_=''
                    )
                break  
   
sendit()
