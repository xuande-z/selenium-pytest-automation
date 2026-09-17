from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """SauceDemo Checkout 页面"""

    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    def input_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        """填写 Checkout 用户信息"""

        self.input(
            self.FIRST_NAME,
            first_name
        )

        self.input(
            self.LAST_NAME,
            last_name
        )

        self.input(
            self.POSTAL_CODE,
            postal_code
        )

    def click_continue(self):
        """进入订单确认页面"""

        self.click(
            self.CONTINUE_BUTTON
        )

        self.wait_for_url_contains(
            "checkout-step-two.html"
        )