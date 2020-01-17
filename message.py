
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACe4f3ce204efc2c5b4404bcb8aeb895dc"
# Your Auth Token from twilio.com/console
auth_token  = "1019d5579b0379d9f36c3b3ebdfae14b"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    body = "Puchica",
    to="++34644964208",
    from_="+17252667058")

print(message.sid)
