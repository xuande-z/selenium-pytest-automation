import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """每条测试用例创建一个独立浏览器"""

    print("\n创建浏览器")

    driver = webdriver.Chrome()

    yield driver

    print("关闭浏览器")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    如果测试执行失败：

    1. 保存失败截图到 screenshots
    2. 把截图以 Base64 方式嵌入 HTML 报告
    """

    outcome = yield
    report = outcome.get_result()

    # 只处理测试函数真正执行的阶段
    if report.when != "call" or not report.failed:
        return

    # 获取当前测试的 driver
    driver = item.funcargs.get("driver")

    if driver is None:
        return

    # =========================
    # 1. 保存本地截图
    # =========================

    screenshots_dir = "screenshots"

    os.makedirs(
        screenshots_dir,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    safe_test_name = (
        item.name
        .replace("[", "_")
        .replace("]", "")
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
    )

    screenshot_path = os.path.join(
        screenshots_dir,
        f"{safe_test_name}_{timestamp}.png"
    )

    driver.save_screenshot(
        screenshot_path
    )

    print(
        f"\n测试失败，截图已保存：{screenshot_path}"
    )

    # =========================
    # 2. 嵌入 HTML 报告
    # =========================

    pytest_html = (
        item.config
        .pluginmanager
        .getplugin("html")
    )

    if pytest_html is None:
        return

    extras = getattr(
        report,
        "extras",
        []
    )

    # Selenium 直接获取 Base64 截图
    screenshot_base64 = (
        driver.get_screenshot_as_base64()
    )

    extras.append(
        pytest_html.extras.image(
            screenshot_base64,
            mime_type="image/png",
            extension="png",
            name="失败截图"
        )
    )

    report.extras = extras