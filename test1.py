# -*- coding:utf-8 -*

import hashlib
import json
import unittest
from urlparse import urljoin

import HTMLTestRunner
# try:
#     from urlparse import urljoin
# except ImportError:
#     from urllib.parse import urljoin
import requests


class DemoApi(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        """
        url = urljoin(self.base_url, "user/login")
        headers = {'Content-Type': 'application/json'}
        data = {"deviceId": "289bf618-8874-4e1c-8b72-7aceb29fa9e2", "password": password,
                "smsCode": "", "terminalType": "3", "userName": username}
        return requests.post(url, headers=headers, data=json.dumps(data)).json()

    def get_token(self, username, password):
        """
        获取登录token
        """
        url = urljoin(self.base_url, "user/login")
        headers = {'Content-Type': 'application/json'}
        data = {"deviceId": "289bf618-8874-4e1c-8b72-7aceb29fa9e2", "password": password,
                "smsCode": "", "terminalType": "3", "userName": username}

        jsonData = requests.post(url, headers=headers, data=json.dumps(data)).json()
        text = json.loads(json.dumps(jsonData))
        data = text['data']
        print 'data=', data
        token = data['token']
        return token

    def banner(self, token):
        """
        banner接口
        """
        url = urljoin(self.base_url, "activity/slideShow/listF")
        headers = {'Content-Type': 'application/json', 'token': token}
        return requests.post(url=url, headers=headers, data={}).json()

    def md5_hexdigest(self, password):
        m = hashlib.md5()  # 创建md5对象
        m.update(password)  # 生成加密串，其中password是要加密的字符串
        password = m.hexdigest()
        return password

    def get_sms_code(self, username, operateType):
        url = urljoin(self.base_url, 'user/getSmsCode')
        headers = {'Content-Type': 'application/json'}
        data = {"phone": username, "operateType": operateType, "userId": "", "ip": "127.0.0.1"}
        return requests.post(url=url, headers=headers, data=json.dumps(data)).json()

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://api.front.jinyoufarm.cn/api/'
        cls.username = '13800138004'
        cls.password = '111111'
        cls.operateType = 0
        cls.app = DemoApi(cls.base_url)

    def test_login(self):
        """
        测试登录
        """
        password = self.app.md5_hexdigest(self.password)
        response = self.app.login(self.username, password)
        print 'login_response', response
        assert response['result'] == 0
        assert response['msg'] == u'成功'

    def test_info(self):
        """
        测试获取banner信息
        """
        password = self.app.md5_hexdigest(self.password)
        token = self.app.get_token(self.username, password)
        response = self.app.banner(token)
        assert response['result'] == 0
        assert response['msg'] == u'OK'

    def test_sms_code(self):
        """"
        测试获取验证码
        """
        response = self.app.get_sms_code(self.username, self.operateType)
        print response
        assert response['result'] == 0
        assert response['msg'] == u'成功'
        assert response['data'] == u'666666'


def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestLogin("test_login"))
    suiteTest.addTest(TestLogin("test_info"))
    suiteTest.addTest(TestLogin("test_sms_code"))
    return suiteTest


if __name__ == "__main__":
    print '__main__'
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(suite())
    file_path = 'C:\\1\\test_result.html'
    fp = file(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告标题', description=u'测试报告详情:')
    runner.run(suiteTest)
    fp.close()
