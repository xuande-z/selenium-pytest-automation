from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    """SauceDemo Checkout Overview 页面"""

    PAGE_TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    ITEM_NAME = (
        By.CSS_SELECTOR,
        '[data-test="inventory-item-name"]'
    )

    ITEM_PRICE = (
        By.CSS_SELECTOR,
        '[data-test="inventory-item-price"]'
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    def get_page_title(self):
        """获取 Overview 页面标题"""

        return self.get_text(
            self.PAGE_TITLE
        )

    def get_item_name(self):
        """获取订单中的商品名称"""

        return self.get_text(
            self.ITEM_NAME
        )

    def get_item_price(self):
        """获取订单中的商品价格"""

        return self.get_text(
            self.ITEM_PRICE
        )

    def click_finish(self):
        """完成订单"""

        self.click(
            self.FINISH_BUTTON
        )

        self.wait_for_url_contains(
            "checkout-complete.html"
        )