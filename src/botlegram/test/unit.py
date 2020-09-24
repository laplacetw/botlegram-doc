#!usr/bin/python3
# coding:utf-8
import unittest
import requests as rq

class SendTestCase(unittest.TestCase):

    def setUp(self):
        self.token = input("token: ")
        self.chat_id = input("chat id: ")
        self.API = "https://api.telegram.org/bot" + token + "/"

    def tearDown(self):
        pass

    def test_send_message(self):
        pass