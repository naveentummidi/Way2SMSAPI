'''
Coded By: Naveen Tummidi
At: 10 November 2019 2:30 PM

This Project is An unofficial API for way2sms website to send messages from your python programs.

'''

from time import sleep
import requests
import re


class Way2Sms:

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def __init__(self, mobile_number, password):

        self.__mobile_no = str(mobile_number);
        self.__password = password
        self.__login_url = 'https://www.way2sms.com/re-login'
        self.__token_url = 'https://www.way2sms.com/send-sms'
        self.__token = ''
        self.__msg_url = 'https://www.way2sms.com/smstoss'
        self.__session = requests.session()
        self.login()
        self.get_Token()

    def login(self):

        login = self.__session.post(self.__login_url, data={'mobileNo': self.__mobile_no, 'password': self.__password, 'CatType': '', 'redirectPage': '', 'pid': ''}, headers=self.headers)
        if login.content != 'send-sms':
            print login.content
            raise Exception('Invalid Credentials')
        else:
            print '\nLogin Success'

    def get_Token(self):

        sleep(2)
        token_data = self.__session.get(self.__token_url).content
        self.__token = re.findall(r'[A-Z\d]{32}', token_data)[0]
        
    def send_sms(self, toMobile, message, ssaction='Undefined', senderId = 'WAYSMS'):

        status = self.__session.post(self.__msg_url, data={'toMobile': str(toMobile), 'Token': self.__token, 'ssaction': ssaction, 'message': message, 'senderId': senderId})
        if status == '0':
            print '\nSMS Sent'
            sleep(1)
        else:
            print '\nSMS Quota Exceeded \U+1F611'



