from twilio.rest import Client as cli
import os

class Client:
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_AUTH']
    def __init__(self):
        self.client = cli(self.account_sid, self.auth_token)

    def send_message(self, _to, msg):
        try:
            message = self.client.messages \
                            .create(
                                body=msg,
                                from_='+17819964562',
                                to=_to
                            )
            return message.sid
        except:
            return None
