from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class WebFormPage(BasePage):

    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    TEXT_BOX = (By.NAME, "my-text")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")
    MESSAGE = (By.ID, "message")

    def open_page(self):
        """打开 Web Form 页面"""
        self.open(self.URL)

    def input_text(self, text):
        """输入文字"""
        self.input(self.TEXT_BOX, text)

    def get_input_value(self):
        """获取输入框当前 value"""
        return self.get_attribute(
            self.TEXT_BOX,
            "value"
        )

    def click_submit(self):
        """点击提交按钮"""
        self.click(self.SUBMIT_BUTTON)

    def get_message(self):
        """获取提交结果"""
        return self.get_text(self.MESSAGE)