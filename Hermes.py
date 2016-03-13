import re

WORDS = ["SEND","TEXT","MESSAGE"]


def isValid(text):
    return bool(re.search(r'\bsend text message\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    
    account_sid = profile["TWILIO_ACCOUNT_SID"]
    auth_token = profile["TWILIO_AUTH_TOKEN"]

    mic.say("Who would you like to send it to?")

    #contact = mic.activeListen()
    contact = "MOM"
    phone_number = getPhoneNumber(contact, profile)    

    print phone_number

    message = "Sending text message"
    mic.say(message)

def getPhoneNumber(contact, profile):
    return profile["TWILIO_CONTACTS"][contact]

def sendSMS():
    return 1





