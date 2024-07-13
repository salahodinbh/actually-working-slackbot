The variables in .env are purely for testing hence no harm in exposing them. For production systems these should not be in no way exposed.
To operate this bot:
- Installing slack's packages through pip is required
- Installing Flask is required
- Installing dotenv is required
- Ngrok is required

Brief steps:
- Create an app in Slack, select it as bot user and install it into your desired workspace
- Give it scopes to check chat history and channels
- Manage events: add the request url obtained from running ngrok in the port used by Flask when running the bot
- Manage events: add event in message.channels
- Enjoy
