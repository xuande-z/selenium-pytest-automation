import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


def test_no_such_element_exception(driver):

    page = BasePage(driver)

    # 1. 打开页面
    page.open(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    print("\n页面已打开")

    # 2. 故意直接寻找一个不存在的元素
    wrong_id = "this-element-does-not-exist"

    print("直接查找不存在的元素...")

    # 3. 预期 Selenium 抛出 NoSuchElementException
    with pytest.raises(NoSuchElementException):

        driver.find_element(
            By.ID,
            wrong_id
        )

    print("成功捕获 NoSuchElementException")
    print("测试继续正常执行")