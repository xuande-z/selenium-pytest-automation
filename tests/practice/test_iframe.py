from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_iframe(driver):

    page = BasePage(driver)

    # 1. 打开 Selenium iframe 测试页面
    page.open(
        "https://www.selenium.dev/selenium/web/iframes.html"
    )

    print("\n打开主页面")

    # 2. iframe 定位器
    iframe = (By.ID, "iframe1")

    # 3. 切换进入 iframe
    page.switch_to_frame(iframe)

    print("已进入 iframe")

    # 4. 获取 iframe 里的元素
    email = driver.find_element(
        By.ID,
        "email"
    )

    email.send_keys("test@example.com")

    # 5. 验证输入成功
    assert email.get_attribute("value") == "test@example.com"

    print("iframe 内元素操作成功")

    # 6. 切回主页面
    page.switch_to_default_content()

    print("已切回主页面")