from twilio.rest import Client
import schedule
import time

# Your Account SID from twilio.com/console
account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
# Your Auth Token from twilio.com/console
auth_token  = "ebc4de3f9adf4794efe5722c8f7ea977"

client = Client(account_sid, auth_token)
numbers = ["720 383 3726", "719 985 5619", "970 978 7468"]

def show_name():
    for number in numbers:
        message = client.messages.create(
        to=number,
        from_="+13148873334",
        body="This is testing Jupyter (1 text per minute)! Free the Tate brothers")
        print(message.sid)
    print("This is working on a 1 min schedule")
    
schedule.every(60).seconds.do(show_name)

while 1:
    schedule.run_pending()
    time.sleep(1)
