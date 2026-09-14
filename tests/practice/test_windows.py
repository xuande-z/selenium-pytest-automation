from pages.base_page import BasePage


def test_window_switch(driver):

    page = BasePage(driver)

    # 1. 打开第一个页面
    page.open("https://www.selenium.dev/")

    # 2. 获取当前窗口
    first_window = page.get_current_window()

    print("\n第一个窗口：", first_window)

    # 3. 保存当前所有窗口
    old_windows = page.get_all_windows()

    print("打开新窗口前：", old_windows)

    # 4. 使用 Selenium 打开一个新的标签页
    driver.switch_to.new_window("tab")

    # 5. 新标签页打开 Python 官网
    page.open("https://www.python.org/")

    # 6. 获取第二个窗口
    second_window = page.get_current_window()

    print("第二个窗口：", second_window)

    # 7. 检查两个窗口不是同一个
    assert first_window != second_window

    print("新窗口切换成功")

    # 8. 检查当前页面
    assert "Python" in driver.title

    print("第二个页面验证成功：", driver.title)

    # 9. 切回第一个窗口
    page.switch_to_window(first_window)

    print("已切回第一个窗口")

    # 10. 验证第一个页面
    assert "Selenium" in driver.title

    print("第一个页面验证成功：", driver.title)