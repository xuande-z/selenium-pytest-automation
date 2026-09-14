from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_new_window(driver):

    page = BasePage(driver)

    # 1. 打开 Selenium 官方测试页面
    page.open(
        "https://www.selenium.dev/selenium/web/window_switching_tests/page_with_frame.html"
    )

    # 2. 记录当前窗口
    first_window = page.get_current_window()

    print("\n原窗口：", first_window)

    # 3. 保存打开新窗口之前的所有窗口
    old_windows = page.get_all_windows()

    print("打开前窗口数量：", len(old_windows))

    # 4. 点击会打开新窗口的链接
    new_window_link = (By.LINK_TEXT, "Open new window")
    page.click(new_window_link)

    # 5. 等待新窗口出现，并自动切换过去
    second_window = page.switch_to_new_window(old_windows)

    print("新窗口：", second_window)

    # 6. 获取现在所有窗口
    new_windows = page.get_all_windows()

    print("打开后窗口数量：", len(new_windows))

    # 7. 验证确实出现了第二个窗口
    assert len(new_windows) == 2

    # 8. 验证已经切换到新窗口
    assert page.get_current_window() == second_window

    print("已成功识别并切换到新窗口")

    # 9. 切回原窗口
    page.switch_to_window(first_window)

    # 10. 验证已经回到原窗口
    assert page.get_current_window() == first_window

    print("已成功切回原窗口")