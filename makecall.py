import os
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='',
                        from_=''
                    )

