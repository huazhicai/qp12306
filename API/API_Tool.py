import json

from PyQt5.Qt import *
import requests


class API(object):
    # 下载验证码
    GET_YZM_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    # 验证码校验
    CHECK_YZM_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    # 登录验证 POST
    # username: 936@qq.com
    # password: 123234
    # appid: otn
    CHECK_ACCOUNT_PWD_URL = 'https://kyfw.12306.cn/passport/web/login'


class APITool(QObject):
    session = requests.session()

    @classmethod
    def download_yzm(cls):
        response = cls.session.get(API.GET_YZM_URL)
        with open('../API/yzm.jpg', 'wb') as f:
            f.write(response.content)

        return "../API/yzm.jpg"

    @classmethod
    def check_yzm(cls, yzm):
        post_data = {
            'answer': yzm,
            'login_site': 'E',
            'rand': 'sjrand'
        }
        response = cls.session.post(API.CHECK_YZM_URL, data=post_data)
        result = json.loads(response.text, encoding="utf-8")
        return result["result_code"] == "4"

    @classmethod
    def check_account_pwd(cls, account, pwd):
        headers = {
            "Host": "kyfw.12306.cn",
            "Connection": "keep-alive",
            "Origin": "https://kyfw.12306.cn",
            "Referer": "https://kyfw.12306.cn/otn/login/init",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        post_data = {
            'username': account,
            'password': pwd,
            'appid': 'otn'
        }
        response = cls.session.post(API.CHECK_ACCOUNT_PWD_URL, data=post_data, headers=headers)
        # dic = response.json()
        # print(dic)
        print(response.text)
        print(type(response.text))


if __name__ == '__main__':
    APITool.download_yzm()
