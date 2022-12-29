from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
# Your Auth Token from twilio.com/console
auth_token  = "ebc4de3f9adf4794efe5722c8f7ea977"

client = Client(account_sid, auth_token)
numbers = ["720 383 3726", "719 985 5619"]
for number in numbers:
  message = client.messages.create(
      to=number,
      from_="+13148873334",
      body="Hurry the fuck up")
  print(message.sid)
