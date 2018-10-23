# Install the Twilio Python library with `pip install --user twilio` in Terminal
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'YOUR SID HERE'
auth_token = 'YOUR TOKEN HERE'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="You have an assignment due in two days. It's: Turn in your Dictionary assignment",
                     from_='', # your Twilio number that you got
                     to='' # Your own phone number
                     )
