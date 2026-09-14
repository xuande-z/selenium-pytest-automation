from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_alert(driver):

    page = BasePage(driver)

    page.open(
        "https://www.selenium.dev/selenium/web/alerts.html"
    )

    alert_button = (By.ID, "alert")

    page.click(alert_button)

    print("\nAlert 已弹出")

    alert_text = page.get_alert_text()

    print("Alert 内容：", alert_text)

    assert alert_text == "cheese"

    page.accept_alert()

    print("普通 Alert 测试通过")


def test_confirm_dismiss(driver):

    page = BasePage(driver)

    page.open(
        "https://www.selenium.dev/selenium/web/alerts.html"
    )

    confirm_button = (By.ID, "confirm")

    page.click(confirm_button)

    print("\nConfirm 已弹出")

    confirm_text = page.get_alert_text()

    print("Confirm 内容：", confirm_text)

    assert confirm_text == "Are you sure?"

    # 点击取消
    page.dismiss_alert()

    print("Confirm 已点击取消")