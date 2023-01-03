from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
# Your Auth Token from twilio.com/console
auth_token  = "ebc4de3f9adf4794efe5722c8f7ea977"

with open("finalSMS.txt", "r") as f:
    lines = f.readlines()

non_empty_lines = [line.strip() for line in lines if line.strip()]
sms = ""

for line in non_empty_lines:
  sms += line + "\n\n"

client = Client(account_sid, auth_token)
numbers = ["720 383 3726", "719 985 5619", "970 978 7468"]

for number in numbers:
  message = client.messages.create(
      to=number,
      from_="+13148873334",
      body=sms)
  print(message.sid)
