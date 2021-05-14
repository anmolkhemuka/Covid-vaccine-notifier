#!/usr/bin/env python3
import urllib.request
import threading
import smtplib
import ssl
import requests
import json     
import os
def telegram_bot_sendtext(bot_message,bot_chatID):
    
    bot_token = '############'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
counter=0

# This function repeatedly reads the Cowin website, and if any appointments are
def sendit():

    global counter
    req = urllib.request.Request('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=462022&date=14-05-2021',headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'})
    html= urllib.request.urlopen(req).read()
    a = json.loads(html)
    test = True
    for p in  a['centers']:
        for s in p['sessions']:
            message="Vaccine available in \n"
            if  s['min_age_limit'] ==18 and s['available_capacity']>0:
                print(p['name'])
                message = message+p['name']+"\non"+s['date']    
                telegram_bot_sendtext(message,'@bhopalu45')
                test=False
               
                break
    if(not test):
        threading.Timer(120.0, sendit).start()
    else:
        threading.Timer(5.0, sendit).start()


    if(test and counter%4000==0):       
        telegram_bot_sendtext("testing",'@testingvaccine')
        counter=0
    counter = counter+1


sendit()

        




