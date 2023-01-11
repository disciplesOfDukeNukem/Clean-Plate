from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
# Your Auth Token from twilio.com/console
auth_token  = "ebc4de3f9adf4794efe5722c8f7ea977"

client = Client(account_sid, auth_token)
numbers = ["720 383 3726", "719 985 5619"]
"""
for number in numbers:
  message = client.messages.create(
      to=number,
      from_="+13148873334",
      body="This is testing GCP minutely exports. I'm prone and ready to bone!")
  print(message.sid)
"""

twilio_lines = []
with open("finalSMS.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line and "No Food/Drink".lower() not in line.lower() and "none" not in line.lower():
            twilio_lines.append(line.replace("[","").replace("]",""))

sms_body = "\n\n".join(twilio_lines)
from twilio.rest import Client
account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
auth_token  = "ebc4de3f9adf4794efe5722c8f7ea977"
client = Client(account_sid, auth_token)
numbers = ["720 383 3726", "719 985 5619"]

for number in numbers:
    message = client.messages.create(
        to=number,
        from_="+13148873334",
        body=sms_body)
    print(message.sid)


##exports.minutelyTask = functions.pubsub.schedule('* * * * *').onRun((context) => {
##    // code to be executed every minute goes here
##    # Your Account SID from twilio.com/console
##    account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
##    # Your Auth Token from twilio.com/console
##    auth_token  = "ebc4de3f9adf4794efe5722c8f7ea977"
##
##    client = Client(account_sid, auth_token)
##    numbers = ["720 383 3726", "719 985 5619", "970 978 7468"]
##
##    for number in numbers:
##        message = client.messages.create(
##        to=number,
##        from_="+13148873334",
##        body="This is testing GCP minutely exports. I'm prone and ready to bone!")
##    print(message.sid)
##});
