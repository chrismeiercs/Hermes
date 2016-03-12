import re

WORDS = ["SEND","TEXT","MESSAGE"]


def isValid(text):
    return bool(re.search(r'\bsend text message\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    message = "Sending text message"
    mic.say(message)





