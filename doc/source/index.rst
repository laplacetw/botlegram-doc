.. Botlegram documentation master file, created by
   sphinx-quickstart on Tue Sep 15 09:47:35 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Botlegram: Telegram Bot Package for Python
==========================================
- Release v0.0.2
- Based on `Telegram Bot API <https://core.telegram.org/bots/api>`_.
- Source code: `laplacetw/botlegram <https://github.com/laplacetw/botlegram>`_
- Stay flexible and keep function naming consistent with the API.

It's good to use. 🙆‍♂️

- Quick Start

.. code:: python

   import botlegram

   BOT_TOKEN = "{{your_bot_token}}"
   WEBHOOK = "{{your_host}}" + BOT_TOKEN + '/'
   bot = botlegram.Bot(BOT_TOKEN, WEBHOOK)
   >>> * [Bot] Webhook is already set

Now we have a Telegram bot 🤖

.. note::

   If you'd like to make sure that the Webhook request comes from Telegram, \
   we recommend using a secret path in the URL, e.g. https://www.example.com/<token>. \
   Since nobody else knows your bot's token, you can be pretty sure it's from Telegram.

   Ref. https://core.telegram.org/bots/api#setwebhook

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   bot
   send
   exception
   release

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
