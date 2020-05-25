import os,sys
sys.path.append(os.getcwd())
import allure
import pytest
from base.base_driver import init_driver
from page.login_page import LoginPage
from base.base_yml import yml_data_with_filename_key

def data_with_key(key):
    return yml_data_with_filename_key("login_data", key)

class Testlogin():

    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize(("username", "password", "toast"), [("188", "123", "成功"), ("188", "321", "成功")])
    @allure.step(title="测试登录脚本")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        is_screen = args["is_screen"]
        screen_filename = args["screen_filename"]

        # 输入手机号
        allure.attach(username, "输入用户名")
        self.login_page.input_username(username)
        # 输入密码
        allure.attach(password, "输入密码")
        self.login_page.input_password(password)
        # 点击登录
        allure.attach('', "点击登录")
        self.login_page.click_login()
        # 判断是否登录成功
        allure.attach(toast, "判断对应提示是否正确")
        result = self.login_page.is_toast_exist(toast, is_screenshot=is_screen, screenshot_name=screen_filename)
        if is_screen:
            allure.attach(open('./screen/' + screen_filename + '.png', 'rb').read(), "图片", attachment_type=allure.attachment_type.PNG)
        assert result