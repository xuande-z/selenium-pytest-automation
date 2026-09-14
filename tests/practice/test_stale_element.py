import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import BasePage


def test_stale_element_exception(driver):

    page = BasePage(driver)

    # 1. 打开页面
    page.open(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    print("\n页面已打开")

    # 2. 第一次定位输入框
    text_box = driver.find_element(
        By.NAME,
        "my-text"
    )

    print("第一次定位元素成功")

    # 3. 使用这个元素
    text_box.send_keys("Before Refresh")

    print("刷新前输入成功")

    # 4. 刷新整个页面
    driver.refresh()

    print("页面已刷新")

    # 5. 页面刷新后，text_box 还是旧 DOM 中的元素对象
    #    再操作它，预期发生 StaleElementReferenceException
    with pytest.raises(StaleElementReferenceException):

        text_box.send_keys("After Refresh")

    print("成功捕获 StaleElementReferenceException")

    # 6. 正确处理方式：重新定位
    new_text_box = driver.find_element(
        By.NAME,
        "my-text"
    )

    new_text_box.send_keys("After Refresh")

    print("重新定位元素成功")

    # 7. 验证新的元素可以正常使用
    actual_value = new_text_box.get_attribute("value")

    print("输入框当前内容：", actual_value)

    assert actual_value == "After Refresh"

    print("Stale 元素重新定位处理成功")