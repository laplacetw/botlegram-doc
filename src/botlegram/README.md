![](https://img.shields.io/github/license/laplacetw/botlegram) [![Documentation Status](https://readthedocs.org/projects/botlegram/badge/?version=latest)](https://botlegram.readthedocs.io/en/latest/?badge=latest)

# Botlegram
A Telegram Bot Package for Python.

- Based on [Telegram Bot API](https://core.telegram.org/bots/api).
- Stay flexible and keep function naming consistent with the API.
- Release v0.0.1

It’s good to use. 🙆‍♂️

### Quick Start

    import botlegram

    BOT_TOKEN = "{{your_bot_token}}"
    WEBHOOK = "{{your_host}}" + BOT_TOKEN + '/'
    bot = botlegram.Bot(BOT_TOKEN, WEBHOOK)
    >>> * [Bot] Webhook is already set

Now we have a Telegram bot 🤖

### Try it on Heroku
- [echo Bot](https://github.com/laplacetw/botlegram/files/5236011/echoBot.zip)

### Read The Docs

[https://botlegram.readthedocs.io/](https://botlegram.readthedocs.io/)