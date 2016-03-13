import re

from twilio.rest import TwilioRestClient

WORDS = ["SEND","TEXT","MESSAGE"]


def isValid(text):
    return bool(re.search(r'\bsend text message\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    
    account_sid = profile["TWILIO_ACCOUNT_SID"]
    auth_token = profile["TWILIO_AUTH_TOKEN"]

    client = TwilioRestClient(account_sid, auth_token);


    #mic.say("Who would you like to send it to?")

    #contact = mic.activeListen()
    contact = "MOM"
    contact_number = getContactNumber(contact, profile)    
    my_number = getMyNumber(profile)
   
    sendSMS(mic, client, contact_number, my_number)

    message = "Sending text message"
    mic.say(message)

def getContactNumber(contact, profile):
    return profile["TWILIO_CONTACTS"][contact]

def getMyNumber(profile):
    return profile["TWILIO_PHONE_NUMBER"]

def sendSMS(mic, client, to_phone_number, from_phone_number):

    mic.say("What would you like to say?")

    #make it all lowercase so it doesn't seem like we're shouting
    message = mic.activeListen().lower()    

    client.messages.create(to=to_phone_number, from_=from_phone_number, body=message)





