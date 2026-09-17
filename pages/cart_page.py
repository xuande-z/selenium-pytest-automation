from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """SauceDemo 购物车页面"""

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

    ITEM_QUANTITY = (
        By.CSS_SELECTOR,
        '[data-test="item-quantity"]'
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    def get_page_title(self):
        """获取购物车页面标题"""
        return self.get_text(
            self.PAGE_TITLE
        )

    def get_item_name(self):
        """获取商品名称"""
        return self.get_text(
            self.ITEM_NAME
        )

    def get_item_price(self):
        """获取商品价格"""
        return self.get_text(
            self.ITEM_PRICE
        )

    def get_item_quantity(self):
        """获取商品数量"""
        return self.get_text(
            self.ITEM_QUANTITY
        )

    def click_checkout(self):
        """点击 Checkout"""

        self.click(
            self.CHECKOUT_BUTTON
        )

        self.wait_for_url_contains(
            "checkout-step-one.html"
        )