import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


# =========================
# 测试数据路径
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent
LOGIN_DATA_FILE = BASE_DIR / "data" / "login_data.json"


def load_login_data():
    """读取登录异常测试数据"""

    with open(
        LOGIN_DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


# =========================
# 正常登录
# =========================

def test_valid_login(driver):
    """验证正确用户名和密码可以成功登录"""

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_page()

    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    print(
        "\n登录后的 URL：",
        driver.current_url
    )

    # 验证 URL
    assert "inventory.html" in driver.current_url

    # 验证商品页面标题
    title = inventory_page.get_product_title()

    print(
        "商品页面标题：",
        title
    )

    assert title == "Products"

    print(
        "登录成功，商品页面验证通过"
    )


# =========================
# 异常登录 - 数据驱动
# =========================

@pytest.mark.parametrize(
    "test_data",
    load_login_data(),
    ids=lambda data: data["case"]
)
def test_invalid_login(driver, test_data):
    """使用 JSON 数据批量验证异常登录场景"""

    login_page = LoginPage(driver)

    login_page.open_page()

    login_page.login(
        username=test_data["username"],
        password=test_data["password"]
    )

    actual_error = (
        login_page.get_error_message()
    )

    expected_error = (
        test_data["expected_error"]
    )

    print(
        "\n测试场景：",
        test_data["case"]
    )

    print(
        "实际错误提示：",
        actual_error
    )

    print(
        "预期包含内容：",
        expected_error
    )

    assert expected_error in actual_error

    print(
        "异常登录场景验证通过"
    )