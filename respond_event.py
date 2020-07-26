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
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    anoop = "U018746RDLY"
    abhi = "U018857RF32"
    Arjun = "U017F3DQL83"
    # slack_client.chat_delete(channel=message["channel"],ts=message['ts'],as_user = True)
    if message.get("subtype") is None and "hi" in message.get('text').lower() and message['user'] != Arjun:
        channel = message["channel"]
        message = "lol <@%s>! ur so funny man" % message["user"]
        slack_client.chat_postMessage(channel=channel, text=message)
        #slack_client.chat_postMessage(channel=channel, text="hi this code was watermarked")
    elif message['user'] == Arjun:
        channel = message["channel"]
        upperlowercase = (message.get('text'))
        newPhrase = ""
        i = True
        for char in upperlowercase:
            if i:
                newPhrase += char.upper()
            else:
                newPhrase += char.lower()
            if char != ' ':
                i = not i
        slack_client.chat_postMessage(channel=channel, text=(newPhrase))

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)