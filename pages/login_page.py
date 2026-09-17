from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """SauceDemo 登录页面"""

    URL = "https://www.saucedemo.com/"

    # =========================
    # 页面元素
    # =========================

    USERNAME = (By.ID, "user-name")

    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        '[data-test="error"]'
    )

    # =========================
    # 页面操作
    # =========================

    def open_page(self):
        """打开登录页面"""
        self.open(self.URL)

    def input_username(self, username):
        """输入用户名"""
        self.input(
            self.USERNAME,
            username
        )

    def input_password(self, password):
        """输入密码"""
        self.input(
            self.PASSWORD,
            password
        )

    def click_login(self):
        """点击登录按钮"""
        self.click(
            self.LOGIN_BUTTON
        )

    def login(self, username, password):
        """完成一次登录操作"""
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def get_error_message(self):
        """获取登录失败提示"""
        return self.get_text(
            self.ERROR_MESSAGE
        )