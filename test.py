# -*- coding:utf-8 -*

import json
import unittest

import requests


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_url = 'http://api.front.jinyoufarm.cn/api/user/login'
        cls.username = '13800138004'
        cls.password = '96e79218965eb72c92a549dd5a330112'

    def test_login(self):
        """
        测试登录
        """
        headers = {'Content-Type': 'application/json'}
        data = {"deviceId": "289bf618-8874-4e1c-8b72-7aceb29fa9e2", "password": self.password,
                "smsCode": "", "terminalType": "3", "userName": self.username}

        response = requests.post(self.login_url, headers=headers,
                                 data=json.dumps(data)).json()
        # print response.content
        assert response['result'] == 0
        assert response['msg'] == u'成功'
