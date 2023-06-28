from twilio.rest import Client

def send_sms(sms):
    account_sid = "INSERT_ACCOUNT_SID"
    auth_token = "INSERT_AUTH_TOKEN"
    client = Client(account_sid, auth_token)
    numbers = ["INSERT_PHONE_NUMBER", "INSERT_PHONE_NUMBER"]

    sms_body = []
    for line in sms.splitlines():
        if line and "No Food/Drink".lower() not in line.lower() and "none" not in line.lower():
            sms_body.append(line.replace("[","").replace("]",""))

    sms_body = "\n\n".join(sms_body)
    for number in numbers:
        message = client.messages.create(
            to=number,
            from_="INSERT_PHONE_NUMBER",
            body=sms_body)
        print(message.sid)

