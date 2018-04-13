# -*- coding:utf-8 -*

import json
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

    email_client = smtplib.SMTP('smtp.126.com')
    email_client.login('daixu_y@126.com', 'daixu324226218')
    # create msg

    # msg = MIMEMultipart('related')
    # msgtext = MIMEText("这是一封测试邮件:", "html","utf-8")
    # msg.attach(msgtext)

    msg = MIMEText('这是一封测试邮件', 'plain', 'utf-8')
    msg['Subject'] = Header('默认主题', 'utf-8')  # subject
    msg['From'] = 'daixu_y@126.com'
    msg['To'] = '324226218@qq.com'
    email_client.sendmail('daixu_y@126.com', '324226218@qq.com', msg.as_string())

    email_client.quit()
