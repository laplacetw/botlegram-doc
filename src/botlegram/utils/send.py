#!usr/bin/env python3
# coding:utf-8
import sys
import json
import requests as rq

class Send():

    r"""
    A parent class which inherited by class Bot about methods of sending in Telegram Bot API.


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
        Use this method to send text messages.

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

            5. disable_notification (bool):
                optional. Sends the message silently. Users will receive a \
                notification with no sound.

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


    # https://core.telegram.org/bots/api#forwardmessage
    def forward_message(
        self, chat_id, from_chat_id, message_id, 
        disable_notification=False
        ):

        r"""
        Use this method to forward messages of any kind.

        Parameters:

            1. chat_id (int/str):
                Unique identifier for the target chat or username of the target \
                channel (in the format @channelusername).
            
            2. from_chat_id (int/str):
                Unique identifier for the chat where the original message was \
                sent (or channel username in the format @channelusername).

            3. message_id (int):
                Message identifier in the chat specified in from_chat_id.
            
            4. disable_notification (bool):
                optional. Sends the message silently. Users will receive a \
                notification with no sound.

        Return: Message object
        

        """        

        api = self.API + "forwardMessage"
        payload = {
            'chat_id':chat_id,
            'from_chat_id':from_chat_id,
            'message_id':message_id,
            'disable_notification':disable_notification}

        return rq.post(api, data=payload).json()

    
    # https://core.telegram.org/bots/api#sendphoto
    def send_photo(
        self, chat_id, photo, caption=None, parse_mode=None, 
        disable_notification=False, reply_to_message_id=None, 
        reply_markup=None
        ):

        r"""
        Use this method to send photos.

        Parameters:

            1. chat_id (int/str):
                Unique identifier for the target chat or username of the target channel \
                (in the format @channelusername).
            
            2. photo (InputFile/str):
                Photo to send. Pass a file_id as String to send a photo that exists on \
                the Telegram servers (recommended), pass an HTTP URL as a String for \
                Telegram to get a photo from the Internet, or upload a new photo using \
                multipart/form-data.
            
            3. caption (str):
                optional. Photo caption (may also be used when resending photos by \
                file_id), 0-1024 characters after entities parsing.
            
            4. parse_mode (str):
                optional. Mode for parsing entities in the message text. \
                See formatting options for more details.
            
            5. disable_notification (bool):
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

    # https://core.telegram.org/bots/api#sendaudio
    def send_audio(
        self, chat_id, audio, caption=None, parse_mode=None, 
        duration=None, performer=None, title=None, thumb=None, 
        disable_notification=False, reply_to_message_id=None, 
        reply_markup=None
        ):

        r"""
        Use this method to send audio files, if you want Telegram clients \
        to display them in the music player. Your audio must be in the .MP3 \
        or .M4A format. Bots can currently send audio files of up to 50 MB \
        in size, this limit may be changed in the future.
        
        For sending voice messages, use the send_voice() instead.

        Parameters:

            1. chat_id (int/str):
                Unique identifier for the target chat or username of the target channel \
                (in the format @channelusername).
            
            2. audio (InputFile/str):
                Audio file to send. Pass a file_id as String to send an audio file that \
                exists on the Telegram servers (recommended), pass an HTTP URL as a \
                String for Telegram to get an audio file from the Internet, or upload a \
                new one using multipart/form-data.
            
            3. caption (str):
                optional. Audio caption, 0-1024 characters after entities parsing.
            
            4. parse_mode (str):
                optional. Mode for parsing entities in the message text. \
                See formatting options for more details.

            5. duration (int):
                optional. Duration of the audio in seconds.

            6. performer (str):
                optional. Performer.

            7. title (str):
                optional. Track name.
            
            8. thumb (InputFile/str):
                optional. Thumbnail of the file sent; can be ignored if thumbnail \
                generation for the file is supported server-side. The thumbnail \
                should be in JPEG format and less than 200 kB in size. A \
                thumbnail's width and height should not exceed 320. Ignored if \
                the file is not uploaded using multipart/form-data. Thumbnails \
                can't be reused and can be only uploaded as a new file, so you \
                can pass “attach://<file_attach_name>” if the thumbnail was \
                uploaded using multipart/form-data under <file_attach_name>. 
            
            9. disable_notification (bool):
                optional. Sends the message silently. Users will receive a \
                notification with no sound.
            
            10. reply_to_message_id (int):
                optional. If the message is a reply, ID of the original message.
            
            11. reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply):
                optional. Additional interface options. A JSON-serialized \
                object for an inline keyboard, custom reply keyboard, instructions \
                to remove reply keyboard or to force a reply from the user.

        Return: Message object


        """

        api = self.API + "sendAudio"
        payload = {
            'chat_id':chat_id,
            'audio':audio,
            'caption':caption,
            'parse_mode':parse_mode,
            'duration':duration,
            'performer':performer,
            'title':title, 'thumb':thumb,
            'disable_notification':disable_notification,
            'reply_to_message_id':reply_to_message_id,
            'reply_markup':reply_markup}

        return rq.post(api, data=payload).json()


    # https://core.telegram.org/bots/api#sendvoice    
    def send_voice(
        self, chat_id, voice, caption=None, parse_mode=None, 
        duration=None, disable_notification=False, 
        reply_to_message_id=None, 
        reply_markup=None
        ):
        
        r"""
        Use this method to send audio files, if you want Telegram clients \
        to display the file as a playable voice message. For this to work, \
        your audio must be in an .OGG file encoded with OPUS (other formats \
        may be sent as Audio or Document). On success, the sent Message is \
        returned. Bots can currently send voice messages of up to 50 MB in \
        size, this limit may be changed in the future.

        1. chat_id (int/str):
            Unique identifier for the target chat or username of the target channel \
            (in the format @channelusername).

        2. voice (InputFile/str):
            Audio file to send. Pass a file_id as String to send a file that exists \
            on the Telegram servers (recommended), pass an HTTP URL as a String for \
            Telegram to get a file from the Internet, or upload a new one using \
            multipart/form-data.

        3. caption (str):
            optional. Audio caption, 0-1024 characters after entities parsing.
            
        4. parse_mode (str):
            optional. Mode for parsing entities in the message text. \
            See formatting options for more details.

        5. duration (int):
            optional. Duration of the audio in seconds.

        6. disable_notification (bool):
            optional. Sends the message silently. Users will receive a \
            notification with no sound.
            
        7. reply_to_message_id (int):
            optional. If the message is a reply, ID of the original message.
        
        8. reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply):
            optional. Additional interface options. A JSON-serialized \
            object for an inline keyboard, custom reply keyboard, instructions \
            to remove reply keyboard or to force a reply from the user.

        Return: Message object


        """

        api = self.API + "sendVoice"
        payload = {
            'chat_id':chat_id,
            'voice':voice,
            'caption':caption,
            'parse_mode':parse_mode,
            'duration':duration,
            'disable_notification':disable_notification,
            'reply_to_message_id':reply_to_message_id,
            'reply_markup':reply_markup}

        return rq.post(api, data=payload).json()


if __name__ == '__main__':
    pass