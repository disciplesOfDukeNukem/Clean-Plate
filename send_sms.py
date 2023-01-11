from twilio.rest import Client

def send_sms(sms):
    account_sid = "AC54b1eccfa25ab3d29ea309bbc9c50448"
    auth_token = "ebc4de3f9adf4794efe5722c8f7ea977"
    client = Client(account_sid, auth_token)
    numbers = ["720 383 3726", "719 985 5619"]

    sms_body = []
    for line in sms.splitlines():
        if line and "No Food/Drink".lower() not in line.lower() and "none" not in line.lower():
            sms_body.append(line.replace("[","").replace("]",""))

    sms_body = "\n\n".join(sms_body)
    for number in numbers:
        message = client.messages.create(
            to=number,
            from_="+13148873334",
            body=sms_body)
        print(message.sid)

