from slackeventsapi import SlackEventAdapter
from slack import WebClient
import os
import time
import datetime as dt
slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

# Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = WebClient(slack_bot_token)

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    slack_client.chat_postMessage(channel="#slacktest", text='suck my goshdarn tonsils!!')
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    Anoop = "U018746RDLY"
    Abhi = "U018857RF32"
    Arjun = "U017F3DQL83"
    Myrrh = 'U01703Z7LCF'
    funny = ["that's what she said", "thats what she said", ":thats-what-she-said", "stupidity", "Abhi", "hi"]
    # slack_client.chat_delete(channel=message["channel"],ts=message['ts'],as_user = True)
    for not_funny in funny:
        if not_funny == message.get('text').lower():
            j = True
            break
        else:
            j = False
    if message.get("subtype") is None and j == True and message['user'] != Abhi:
        channel = message["channel"]
        message = "lol <@%s>! ur so funny man" % message["user"]
        slack_client.chat_postMessage(channel=channel, text=message)
        #slack_client.chat_postMessage(channel=channel, text="hi this code was watermarked")
    elif message['user'] == Abhi:
        channel = message["channel"]
        upperlowercase = (message.get('text'))
        newPhrase = ""
        if len(upperlowercase) >= 2:
            i = True
            for char in upperlowercase:
                if i:
                    newPhrase += char.lower()
                else:
                    newPhrase += char.upper()
                if char != ' ':
                    i = not i
            slack_client.chat_postMessage(channel=channel, text=(newPhrase))
        else:
            pass
            

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=5000)