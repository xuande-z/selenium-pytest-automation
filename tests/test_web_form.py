import json
from pathlib import Path

import pytest

from pages.web_form_page import WebFormPage


# 获取项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# JSON 测试数据路径
DATA_FILE = BASE_DIR / "data" / "web_form_data.json"


def load_test_data():
    """读取 JSON 测试数据"""

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.mark.parametrize(
    "test_data",
    load_test_data()
)
def test_web_form(driver, test_data):

    # 从 JSON 中取数据
    input_text = test_data["input_text"]
    expected_message = test_data["expected_message"]

    # 创建页面对象
    page = WebFormPage(driver)

    # 打开页面
    page.open_page()

    # 输入文字
    page.input_text(input_text)

    # 验证输入框内容
    actual_input = page.get_input_value()

    print("\n输入的数据：", input_text)
    print("输入框实际内容：", actual_input)

    assert actual_input == input_text

    print("输入验证通过")

    # 点击提交
    page.click_submit()

    # 获取结果
    actual_message = page.get_message()

    print("实际结果：", actual_message)
    print("预期结果：", expected_message)

    assert actual_message == expected_message

    print("提交结果验证通过")