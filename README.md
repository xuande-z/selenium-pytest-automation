# Selenium + Pytest Web Automation Testing Framework

基于 **Python + Selenium + Pytest** 搭建的 Web UI 自动化测试项目。

项目采用 **Page Object Model（POM）** 设计模式，对页面元素、页面操作、测试数据和测试用例进行分层管理，并集成日志、HTML 测试报告、失败自动截图、显式等待、异常处理和数据驱动测试。

目前项目包含 Selenium 官方测试页面练习，以及基于 **SauceDemo** 实现的登录、购物车和完整 Checkout 业务流程自动化测试。

---

## 1. Tech Stack

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- pytest-metadata
- Page Object Model（POM）
- JSON Data Driven Testing
- Git / GitHub

---

## 2. Project Structure

```text
selenium-pytest-automation/
│
├── config/
│   └── settings.py
│
├── data/
│   ├── login_data.json
│   └── web_form_data.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   ├── checkout_complete_page.py
│   └── web_form_page.py
│
├── tests/
│   ├── practice/
│   │   ├── test_alert.py
│   │   ├── test_iframe.py
│   │   ├── test_logger.py
│   │   ├── test_new_window.py
│   │   ├── test_no_such_element.py
│   │   ├── test_stale_element.py
│   │   ├── test_timeout.py
│   │   └── test_windows.py
│   │
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_web_form.py
│
├── utils/
│   └── logger.py
│
├── logs/
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 3. Framework Design

项目采用 Page Object Model（POM）进行页面分层。

```text
Test Cases
    ↓
Page Objects
    ↓
BasePage
    ↓
Selenium WebDriver
    ↓
Browser
```

### BasePage

`BasePage` 封装 Selenium 常用操作，包括：

- 打开页面
- 输入文本
- 点击元素
- 获取元素文本
- 获取元素属性
- URL 显式等待
- iframe 切换
- 多窗口切换
- Alert 操作
- Stale Element 自动重新定位

业务页面继承 `BasePage`，避免在测试用例中重复编写底层 Selenium 操作。

---

## 4. SauceDemo Automation

项目使用 SauceDemo 作为完整业务自动化测试场景。

### Login Testing

登录模块包含正常和异常场景。

覆盖：

- 正确用户名 + 正确密码
- 错误用户名
- 错误密码
- 用户名和密码同时错误
- 用户名为空
- 密码为空
- 用户名和密码同时为空

异常登录数据存放在：

```text
data/login_data.json
```

通过：

```python
@pytest.mark.parametrize
```

实现 JSON 数据驱动测试。

---

## 5. Shopping Cart Testing

购物车自动化流程：

```text
Login
  ↓
Products
  ↓
Add Sauce Labs Backpack
  ↓
Cart Badge = 1
  ↓
Open Cart
  ↓
Verify Product
```

验证内容：

```text
Product:
Sauce Labs Backpack

Price:
$29.99

Quantity:
1
```

---

## 6. End-to-End Checkout Testing

项目实现完整购买流程 E2E 自动化：

```text
Login
  ↓
Products
  ↓
Add Product
  ↓
Shopping Cart
  ↓
Checkout
  ↓
Customer Information
  ↓
Checkout Overview
  ↓
Finish
  ↓
Checkout Complete
```

测试过程中验证：

```text
Products

Your Cart

Sauce Labs Backpack

$29.99

Checkout: Overview

Checkout: Complete!

Thank you for your order!
```

通过 URL 显式等待确保页面导航完成，例如：

```python
self.wait.until(
    EC.url_contains("checkout-step-two.html")
)
```

避免使用固定 `sleep()` 等待页面跳转。

---

## 7. Explicit Wait

框架主要使用：

```python
WebDriverWait
```

配合 Selenium Expected Conditions：

```python
EC.element_to_be_clickable()
EC.visibility_of_element_located()
EC.frame_to_be_available_and_switch_to_it()
EC.new_window_is_opened()
EC.alert_is_present()
EC.url_contains()
```

减少固定等待，提高测试稳定性。

---

## 8. Stale Element Handling

在页面跳转或 DOM 更新过程中，WebElement 可能失效并产生：

```text
StaleElementReferenceException
```

`BasePage.get_text()` 中实现重新定位机制。

当元素失效时：

```text
Locate Element
    ↓
DOM Updated
    ↓
StaleElementReferenceException
    ↓
Retry
    ↓
Locate New Element
    ↓
Get Text
```

从而提高动态页面测试的稳定性。

---

## 9. Pytest Fixture

浏览器生命周期通过 Pytest Fixture 管理。

```python
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
```

每条需要浏览器的测试用例使用独立 WebDriver Session，从而减少测试用例之间的状态污染。

---

## 10. Failure Screenshot

项目使用：

```python
pytest_runtest_makereport
```

监听测试结果。

测试失败时自动：

```text
Test Failed
    ↓
Capture Screenshot
    ↓
Save PNG
    ↓
Convert Screenshot to Base64
    ↓
Embed Screenshot into HTML Report
```

截图保存在：

```text
screenshots/
```

---

## 11. Logging

项目封装统一日志模块：

```text
utils/logger.py
```

日志包含：

```text
Timestamp
Log Level
Page Object
Operation
```

例如：

```text
INFO - LoginPage - 打开页面
INFO - LoginPage - 输入用户名
INFO - LoginPage - 点击登录按钮
INFO - InventoryPage - 获取商品页面标题
```

日志同时输出到：

```text
Console
+
logs/test.log
```

---

## 12. HTML Report

项目使用：

```text
pytest-html
```

自动生成 HTML 测试报告。

配置位于：

```text
pytest.ini
```

测试执行后生成：

```text
reports/report.html
```

失败测试的截图会嵌入 HTML Report，便于定位失败原因。

---

## 13. Exception Handling Practice

项目包含 Selenium 常见异常处理练习：

```text
TimeoutException
NoSuchElementException
StaleElementReferenceException
```

同时包含：

```text
Alert
iframe
Multiple Windows
Window Switching
Explicit Wait
```

等 Selenium 常用场景。

---

## 14. Install

Clone repository:

```bash
git clone https://github.com/xuande-z/selenium-pytest-automation.git
```

进入项目目录：

```bash
cd selenium-pytest-automation
```

创建虚拟环境：

```bash
python -m venv .venv
```

Windows 激活虚拟环境：

```bash
.venv\Scripts\activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

---

## 15. Run Tests

运行全部测试：

```bash
pytest
```

运行登录测试：

```bash
pytest tests/test_login.py
```

运行购物车测试：

```bash
pytest tests/test_cart.py
```

运行完整 Checkout E2E：

```bash
pytest tests/test_checkout.py
```

简洁模式：

```bash
pytest -q
```

---

## 16. Current Test Result

当前完整回归测试结果：

```text
22 passed in 88.29s
```

覆盖内容包括：

```text
Web Form
Login
Login Negative Cases
Shopping Cart
Checkout E2E
Alert
iframe
Multiple Windows
TimeoutException
NoSuchElementException
StaleElementReferenceException
Logging
```

---

## 17. Key Features

- Selenium Web UI Automation
- Pytest Test Framework
- Page Object Model
- BasePage Common Operations
- Explicit Wait
- JSON Data Driven Testing
- Pytest Parameterization
- Fixture Browser Lifecycle
- Logging
- HTML Test Report
- Automatic Failure Screenshot
- Screenshot Embedded in HTML Report
- Selenium Exception Handling
- Stale Element Retry
- Multi-window Testing
- iframe Testing
- Alert Testing
- Complete SauceDemo Checkout E2E Testing

---

## 18. Future Improvements

后续计划：

- API Automation Testing
- Database Validation
- SQL
- Linux
- Docker
- CI/CD
- GitHub Actions
- Parallel Testing
- Environment Configuration
- More Business Test Scenarios