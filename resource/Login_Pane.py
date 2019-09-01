from PyQt5.Qt import *
from resource.login_ui import Ui_Form

from API.API_Tool import APITool


class LoginPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.refresh_yzm()

    def refresh_yzm(self):
        print("验证码")
        url = APITool.download_yzm()
        pixmap = QPixmap(url)
        self.yzm_label.setPixmap(pixmap)
        self.yzm_label.clear_points()

    def auto_dm(self):
        print("自动打码")
        # dm = YDMHttp()
        # result = dm.get_yzm_result(self.)
        # print(result)
        # self.yzm_label.auto_add_point(result)

    def check_login(self):
        print('验证登录')
        result = self.yzm_label.get_result()
        if len(result) == 0:
            print("请填写验证码")
            return None
        if APITool.check_yzm(result):
            print("成功")
            # 账号和密码
            account = self.account_le.text()
            pwd = self.pwd_le.text()
            print(account, pwd)
            APITool.check_account_pwd(account, pwd)
        else:
            print("失败")
            self.yzm_label.clear_points()
            self.refresh_yzm()

    def auto_enable_login_btn(self):
        print("自动设置登录按钮")
        account = self.account_le.text()
        pwd = self.pwd_le.text()
        if len(account) == 0 or len(pwd) == 0:
            self.login_btn.setEnabled(False)
        else:
            self.login_btn.setEnabled(True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    login = LoginPane()

    login.show()
    sys.exit(app.exec_())
