#!usr/bin/env python3
# coding:utf-8
import sys
import json
import requests as rq
from .utils.send import Send
from .exception import WebhookError

class Bot(Send):

    r"""
    The class will execute setting webhook when initialization occurs.

    Parameters:

        1. webhook (str): host webhook
        2. token (str): token of telegram bot

    Inherits from:

        1. class Send


    """

    def __init__(self, token, webhook):
        self.API = "https://api.telegram.org/bot" + token + "/"
        self.WEBHOOK = webhook
        self.SET_WEBHOOK = self.get_webhook_info()['result']['url']

        if self.SET_WEBHOOK != self.WEBHOOK:
            self.set_webhook()
        else:
            self.console_log("Webhook is already set")


    # https://core.telegram.org/bots/api#getwebhookinfo
    def get_webhook_info(self):

        r"""
        For checking webhook setting.

        Return: WebhookInfo object


        """

        api = self.API + "getWebhookInfo"
        return rq.post(api).json()


    # https://core.telegram.org/bots/api#setwebhook
    def set_webhook(self):

        r"""
        For webhook setting.

        Return: True
        
        Exception: WebhookError


        """

        api = self.API + "setWebhook"
        payload = {'url':self.WEBHOOK}
        webhook = rq.post(api, data=payload).json()
        self.console_log(webhook['description'])
        if webhook['ok']:
            return True
        else:
            raise WebhookError(webhook['description'])

    
    def console_log(self, log):

        r"""
        Print any message to logs immediately. e.g. Heroku logs.

        Parameters:

            1. log (str)
        

        """

        print(" * [Bot] " + log)
        sys.stdout.flush()


    # https://core.telegram.org/bots/api#message
    def msg_type(self, request):

        r"""
        For checking message types.

        Parameters:

            1. request (Flask.request object)

        Return: message type(str) or False


        """

        content = request.json
        type_list = [
            'text', 'animation', 'audio', 'document', 'photo', 'sticker', \
            'video', 'video_note', 'voice', 'contact', 'dice', 'game', 'poll', \
            'venue', 'location', 'invoice', 'successful_payment']
        
        for type_ in type_list:
            if type_ in content['message']:
                return type_
        
        return False


if __name__ == '__main__':
    pass