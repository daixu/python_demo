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

        json_data = requests.post(url, headers=headers, data=json.dumps(data)).json()
        text = json.loads(json.dumps(json_data))
        data = text['data']
        print 'data=', data
        token = data['token']
        return token

    def get_user_id(self, username, password):
        """
        获取登录user_id
        """
        url = urljoin(self.base_url, "user/login")
        headers = {'Content-Type': 'application/json'}
        data = {"deviceId": "289bf618-8874-4e1c-8b72-7aceb29fa9e2", "password": password,
                "smsCode": "", "terminalType": "3", "userName": username}

        json_data = requests.post(url, headers=headers, data=json.dumps(data)).json()
        text = json.loads(json.dumps(json_data))
        data = text['data']
        print 'data=', data
        user_id = data['userId']
        return user_id

    def banner(self, token):
        """
        banner接口
        """
        url = urljoin(self.base_url, "activity/slideShow/listF")
        headers = {'Content-Type': 'application/json', 'token': token}
        return requests.post(url=url, headers=headers, data={}).json()

    @staticmethod
    def md5_hexdigest(password):
        m = hashlib.md5()  # 创建md5对象
        m.update(password)  # 生成加密串，其中password是要加密的字符串
        password = m.hexdigest()
        return password

    def get_sms_code(self, username, operate_type):
        """
        获取短信验证码接口
        """
        url = urljoin(self.base_url, 'user/getSmsCode')
        headers = {'Content-Type': 'application/json'}
        data = {"phone": username, "operateType": operate_type, "userId": "", "ip": "127.0.0.1"}
        return requests.post(url=url, headers=headers, data=json.dumps(data)).json()

    def get_address(self, user_id, token):
        """"
        获取商户收货地址
        """
        url = urljoin(self.base_url, "user/userReceivingAddress")
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"userId": user_id}
        return requests.post(url=url, headers=headers, data=json.dumps(data)).json()

    def get_common_list(self, user_id, token):
        """
        获取常用清单
        """
        url = urljoin(self.base_url, "user/commonUserGreensList")
        headers = {'Content-Type': 'application/json', 'token': token}
        data = {"userId": user_id}
        return requests.post(url=url, headers=headers, data=json.dumps(data)).json()


class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://api.front.jinyoufarm.cn/api/'
        cls.username = '13800138004'
        cls.password = '111111'
        cls.operateType = 0
        cls.app = DemoApi(cls.base_url)
        cls.login_response = cls.app.login(cls.username, cls.app.md5_hexdigest(cls.password))

    def test_login(self):
        """
        测试登录
        """
        password = self.app.md5_hexdigest(self.password)
        response = self.app.login(self.username, password)
        print 'login_response', response
        assert response['result'] == 0
        assert response['msg'] == u'成功'

    def test_banner(self):
        """
        测试获取banner信息
        """
        # password = self.app.md5_hexdigest(self.password)
        json_data = self.login_response
        text = json.loads(json.dumps(json_data))
        data = text['data']
        token = data['token']

        # token = self.app.get_token(self.username, password)
        response = self.app.banner(token)
        print 'response=', response
        assert response['result'] == 0
        assert response['msg'] == u'OK'

    def test_sms_code(self):
        """
        测试验证码
        """
        response = self.app.get_sms_code(self.username, self.operateType)
        print response
        assert response['result'] == 0
        assert response['msg'] == u'成功'
        assert response['data'] == u'666666'

    def test_address(self):
        """
        测试获取商户地址
        """
        # password = self.app.md5_hexdigest(self.password)
        # json_data = self.app.login(self.username, password)
        # text = json.loads(json.dumps(json_data))
        # data = text['data']
        # print 'data=', data
        # user_id = data['userId']
        # token = data['token']
        # print 'userId=', user_id
        # print 'token=', token

        json_data = self.login_response
        text = json.loads(json.dumps(json_data))
        data = text['data']
        token = data['token']
        user_id = data['userId']

        response = self.app.get_address(user_id, token)
        print response
        assert response['result'] == 0
        assert response['msg'] == u'成功'

    def test_common_list(self):
        """
        测试常用清单
        """
        # password = self.app.md5_hexdigest(self.password)
        # json_data = self.app.login(self.username, password)
        # text = json.loads(json.dumps(json_data))
        # data = text['data']
        # print 'data=', data
        # user_id = data['userId']
        # token = data['token']
        # print 'userId=', user_id
        # print 'token=', token

        json_data = self.login_response
        text = json.loads(json.dumps(json_data))
        data = text['data']
        token = data['token']
        user_id = data['userId']

        response = self.app.get_common_list(user_id, token)
        print response
        assert response['result'] == 0
        assert response['msg'] == u'成功'


def suite():
    suite_test = unittest.TestSuite()
    # suite_test.addTest(TestApi("test_login"))
    suite_test.addTest(TestApi("test_banner"))
    suite_test.addTest(TestApi("test_sms_code"))
    suite_test.addTest(TestApi("test_address"))
    suite_test.addTest(TestApi("test_common_list"))
    return suite_test


if __name__ == "__main__":
    print '__main__'
    suite_test = unittest.TestSuite()
    suite_test.addTest(suite())
    file_path = 'C:\\1\\test_result.html'
    fp = file(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告标题', description=u'测试报告详情:')
    runner.run(suite_test)
    fp.close()
