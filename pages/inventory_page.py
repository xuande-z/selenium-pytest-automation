from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """SauceDemo 商品列表页面"""

    # =========================
    # 元素定位器
    # =========================

    # 商品页面标题
    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        '[data-test="title"]'
    )

    # Sauce Labs Backpack 加入购物车按钮
    BACKPACK_ADD_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    # 购物车数量角标
    CART_BADGE = (
        By.CSS_SELECTOR,
        '[data-test="shopping-cart-badge"]'
    )

    # 购物车入口
    CART_LINK = (
        By.CSS_SELECTOR,
        '[data-test="shopping-cart-link"]'
    )

    # =========================
    # 页面操作
    # =========================

    def get_product_title(self):
        """获取商品页面标题"""

        return self.get_text(
            self.PRODUCT_TITLE
        )

    def add_backpack_to_cart(self):
        """添加 Sauce Labs Backpack 到购物车"""

        self.click(
            self.BACKPACK_ADD_BUTTON
        )

    def get_cart_count(self):
        """获取购物车商品数量"""

        return self.get_text(
            self.CART_BADGE
        )

    def open_cart(self):
        """进入购物车页面"""

        # 点击购物车
        self.click(
            self.CART_LINK
        )

        # 等待浏览器真正进入购物车页面
        self.wait_for_url_contains(
            "cart.html"
        )