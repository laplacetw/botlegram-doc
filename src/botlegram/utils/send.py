#!usr/bin/env python3
# coding:utf-8
import sys
import json
import requests as rq

class Send():

    r"""
    A parent class about sending methods of Telegram Bot API that inherited by class Bot.


    """

    def __init__(self):
        self.API = ""


    # https://core.telegram.org/bots/api#sendmessage
    def send_message(
        self, chat_id, text, parse_mode=None, 
        disable_web_page_preview=False, 
        disable_notification=False, 
        reply_to_message_id=None, 
        reply_markup=None
        ):

        r"""
        For Sending text message.

        Parameters:

            1. chat_id (int/str):
                Unique identifier for the target chat or username of the target \
                channel (in the format @channelusername).
            
            2. text (str):
                Text of the message to be sent, 1-4096 characters after entities parsing.

            3. parse_mode (str):
                optional. Mode for parsing entities in the message text. \
                See formatting options for more details.
            
            4. disable_web_page_preview (bool):
                optional. Disables link previews for links in this message.

            5. disable_notification (str):
                optional. Sends the message silently. Users will receive a notification with no sound.

            6. reply_to_message_id (int):
                optional. If the message is a reply, ID of the original message.
            
            7. reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply):
                optional. Additional interface options. A JSON-serialized object for an inline \
                keyboard, custom reply keyboard, instructions to remove reply keyboard or to \
                force a reply from the user.

        Return: Message object
        

        """

        api = self.API + "sendMessage"
        payload = {
            'chat_id':chat_id,
            'text':text,
            'parse_mode':parse_mode,
            'disable_web_page_preview':disable_web_page_preview,
            'disable_notification':disable_notification,
            'reply_to_message_id':reply_to_message_id,
            'reply_markup':reply_markup}

        return rq.post(api, data=payload).json()

    
    # https://core.telegram.org/bots/api#sendphoto
    def send_photo(
        self, chat_id, photo, caption=None, parse_mode=None, 
        disable_notification=False, 
        reply_to_message_id=None, 
        reply_markup=None
        ):

        r"""
        For Sending text message.

        Parameters:

            1. chat_id (int/str):
                Unique identifier for the target chat or username of the target channel \
                (in the format @channelusername).
            
            2. photo (InputFile/str):
                hoto to send. Pass a file_id as String to send a photo that exists on \
                the Telegram servers (recommended), pass an HTTP URL as a String for \
                Telegram to get a photo from the Internet, or upload a new photo using \
                multipart/form-data.
            
            3. caption (str):
                optional. Photo caption (may also be used when resending photos by \
                file_id), 0-1024 characters after entities parsing.
            
            4. parse_mode (str):
                optional. Mode for parsing entities in the message text. \
                See formatting options for more details.
            
            5. disable_notification (str):
                optional. Sends the message silently. Users will receive a \
                notification with no sound.
            
            6. reply_to_message_id (int):
                optional. If the message is a reply, ID of the original message.
            
            7. reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply):
                optional. Additional interface options. A JSON-serialized \
                object for an inline keyboard, custom reply keyboard, instructions \
                to remove reply keyboard or to force a reply from the user.

        Return: Message object

        .. note::

            To prevent Telegram url cache, we can put timestamp into the url.
            
            e.g. <photo_url>?timestamp=xxxxxxxxxxx
            
            Ref. `stackoverflow <https://stackoverflow.com/questions/42719409/telegram-bot-image-from-url-undesired-cache>`_
        

        """

        api = self.API + "sendPhoto"
        payload = {
            'chat_id':chat_id,
            'photo':photo,
            'caption':caption,
            'parse_mode':parse_mode,
            'disable_notification':disable_notification,
            'reply_to_message_id':reply_to_message_id,
            'reply_markup':reply_markup}

        return rq.post(api, data=payload).json()


if __name__ == '__main__':
    pass