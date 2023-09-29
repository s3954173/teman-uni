TWILIO_ACCOUNT_SID = 'ACfbf3a2cc00f08043b9f8338c2d952600'
TWILIO_AUTH_TOKEN = '9ef238af45b106606debef26e749368a'
from twilio.rest import Client
from django.cof import settings

def send_otp(phone_number, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    try:
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_='+61415760314',
            to=phone_number,
        )

        return message.sid
    except Exception as e:
        return str(e)