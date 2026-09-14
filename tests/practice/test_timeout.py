import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


def test_timeout_exception(driver):

    page = BasePage(driver)

    # 1. 打开 Selenium 测试页面
    page.open(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    print("\n页面已打开")

    # 2. 故意写一个不存在的元素
    wrong_locator = (
        By.ID,
        "this-element-does-not-exist"
    )

    print("开始等待一个不存在的元素...")

    # 3. 我们明确预期这里应该发生 TimeoutException
    with pytest.raises(TimeoutException):

        page.click(wrong_locator)

    print("成功捕获 TimeoutException")

    print("测试程序没有因为异常直接崩掉")