from twilio.rest import Client
import schedule
import time

# Your Account SID from twilio.com/console
account_sid = "INSERT_ACCOUNT_SID"
# Your Auth Token from twilio.com/console
auth_token  = "INSERT_AUTH_TOKEN"

client = Client(account_sid, auth_token)
numbers = ["INSERT_PHONE_NUMBER", "INSERT_PHONE_NUMBER"]

def show_name():
    for number in numbers:
        message = client.messages.create(
        to=number,
        from_="INSERT_PHONE_NUMBER",
        body="This is testing Jupyter (1 text per minute)! Free the Tate brothers")
        print(message.sid)
    print("This is working on a 1 min schedule")
    
schedule.every(60).seconds.do(show_name)

while 1:
    schedule.run_pending()
    time.sleep(1)
