import slack
from slackeventsapi import SlackEventAdapter
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)

env = ".env"
load_dotenv(env)

client = slack.WebClient(os.environ.get('TRUE_BOT_TOKEN'))
slack_events_adapter = SlackEventAdapter(os.environ.get('SLACK_SIGNING_SECRET'), "/slack/events", app)

# This sends a message everytime the server is initiated and bot is operating
client.chat_postMessage(channel='random',text='Hey I''m here')

# Retrieve the id of the bot so it doesn't handle its own messages
bot_id = client.api_call("auth.test")['user_id']

# This handles incoming messages in a channel and replies to them if they are NOT from the bot
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    channel_id = message["channel"]
    user_id = message["user"]
    text = message.get("text")
    print(f"Received a message from user {user_id} in channel {channel_id}: {text}")

    if user_id != bot_id:
        client.chat_postMessage(channel='random',text=text + ' is a beautiful message')

@app.route("/test")
def epic():
    return "url OK"

# Starts the Flask server in debug mode
if __name__ == "__main__":
    app.run(debug=True, port=3000) 