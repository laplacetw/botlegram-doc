#!usr/bin/python3
# coding:utf-8
import os
import pytest
import requests as rq
from botlegram.utils.send import Send

token = os.environ['TOKEN']
chat_id = os.environ['CHAT_ID']
voice_id = os.environ['VOICE_ID']
audio_id = os.environ['AUDIO_ID']
api = "https://api.telegram.org/bot" + token + "/"
test = Send()
test.API = api

def test_forward_message():
    res = test.forward_message(chat_id, chat_id, 323)
    assert res['ok'] == True

def test_send_voice():
    res = test.send_voice(chat_id, voice_id)
    assert res['ok'] == True

def test_send_audio():
    res = test.send_audio(chat_id, audio_id)
    assert res['ok'] == True

def pass_test_send_message():
    res = test.send_message(chat_id, "test")
    assert res['ok'] == True

def pass_test_send_photo():
    photo = "https://github.com/laplacetw/laplacetw.github.io/blob/master/images/avatar.png"
    res = test.send_photo(chat_id, photo, "laplacetw")
    assert res['ok'] == True