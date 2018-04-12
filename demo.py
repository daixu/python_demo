# -*- coding:utf-8 -*
import json
import requests


def test():
    url = "http://api.front.jinyoufarm.cn/api/user/login"  # 测试的接口url
    headers = {'Content-Type': 'application/json'}
    data = {"deviceId": "289bf618-8874-4e1c-8b72-7aceb29fa9e2", "password": "96e79218965eb72c92a549dd5a330112",
                "smsCode": "", "terminalType": "3", "userName": "13800138004"}
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print 'r.content=', r.content
    print 'r.json=', r.json()
    return r.json()

def test_banner():
    text = json.loads(json.dumps(test()))
    data = text['data']
    token = data['token']
    print 'token=', token
    url = "http://api.front.jinyoufarm.cn/api/activity/slideShow/listF"

    headers = {'Content-Type': 'application/json', 'token': token}
    r = requests.post(url=url, headers=headers, data={})

    print 'r.content=', r.content

if __name__ == "__main__":
    test()
    test_banner()
