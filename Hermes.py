import re

WORDS = ["SEND","TEXT","MESSAGE"]


def isValid(text):
    return bool(re.search(r'\bsend text message\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    
    account_sid = profile["TWILIO_ACCOUNT_SID"]
    auth_token = profile["TWILIO_AUTH_TOKEN"]

    print account_sid
    print auth_token
    

    message = "Sending text message"
    mic.say(message)





