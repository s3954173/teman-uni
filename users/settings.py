import os
from twilio.rest import Client

account_sid = os.environ['AC6fbe71c8458e7cb9d48961a7da613f5d']
auth_token = os.environ['8644438cb8370946e5c49f021392194f']
client = Client(account_sid, auth_token)

verification = client.verify \
                     .v2 \
                     .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .verifications \
                     .create(to='recipient@foo.com', channel='email')

print(verification.sid)
