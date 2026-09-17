from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    """SauceDemo 订单完成页面"""

    PAGE_TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    COMPLETE_HEADER = (
        By.CSS_SELECTOR,
        '[data-test="complete-header"]'
    )

    def get_page_title(self):
        """获取完成页面标题"""

        return self.get_text(
            self.PAGE_TITLE
        )

    def get_complete_message(self):
        """获取订单完成提示"""

        return self.get_text(
            self.COMPLETE_HEADER
        )