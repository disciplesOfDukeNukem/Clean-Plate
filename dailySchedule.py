from twilio.rest import Client
from datetime import datetime
import schedule
import time


# Your Account SID from twilio.com/console
account_sid = "INSERT_ACCOUNT_SID"
# Your Auth Token from twilio.com/console
auth_token  = "INSERT_AUTH_TOKEN"

client = Client(account_sid, auth_token)
numbers = ["INSERT_PHONE_NUMBER", "INSERT_PHONE_NUMBER"]

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


def show_name():
    
    for number in numbers:
        message = client.messages.create(
        to=number,
        from_="+13148873334",
        body="WTF I can't get the daily scheduling to work! It's just like one line of code.")
        print(message.sid)
    print("This is working on a 1 min schedule")

#show_name()
#runs python script daily at 8am MST 15:00 UTC
#schedule.every(day).at("21:00").do(show_name)
schedule.every().day.at("14:22:50").do(show_name)

while 1:
    schedule.run_pending()
    time.sleep(1)
