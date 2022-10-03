# Discord Customizable Chatbot

The chatbot uses a character description (about 50-100 words), and from that generates responses in a discord server. 

## Getting started
This bot allows for users to simply change the characterization script and change the bot's personality.

Dont forget to add your .env file in the main directory. In there paste the following template and replace <YOUR_KEY> with your own key.

```
# .env
DISCORD_TOKEN=<YOUR_KEY>
OPENAI_API_KEY=<YOUR_KEY>
```

Integrate this bot into your server by entering your OpenAI key and your Discord Bot key, and start the program by running the `mail.py` file.

```
python3 mail.py
```
## Required Prerequisites

The following packages need to be installed:
```
pip install discord openai python-dotenv
```

## Configuration

Any configuration can be made in the `Settings.py` file. There you can access settings for:
- Keyword detection
- Character Reference
- Discord API Wait and Typing Indicator settings
- OpenAI model preferences

## API References:

Discord.py: https://discordpy.readthedocs.io/en/stable/api.html

OpenAI https://beta.openai.com/docs/api-reference/edits
