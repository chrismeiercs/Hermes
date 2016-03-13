# Hermes

Register an account with Twilio and create a phone number

Install the Twilio Python Module
```bash
sudo pip install twilio
```

Add your Account SID, Auth Token, and Twilio phone number to your profile.yml
```yml
TWILIO_PHONE_NUMBER: twilio phone number as a string
TWILIO_ACCOUNT_SID: account sid
TWILIO_AUTH_TOKEN: auth token
```
*Be sure to include the country code prefix for all numbers (if you are in the US it it +1)!

With the current implementation, you can only send to people in your contacts list, which is a dictionary containing phone numbers. Create your contacts list in the following manner in your profile.yml (using your parents' numbers as examples):
```yml
TWILIO_CONTACTS{MOM: "+15555555555", DAD: "+14444444444"}
```

To activate Hermes, your sentence must include the phrase "send text message"

To send a text message:
YOU: Send text message
JASPER: Who would you like to send it to?
YOU: Mom
JASPER: What would you like to say?
YOU: Happy Mothers Day!
JASPER: Text message sent
