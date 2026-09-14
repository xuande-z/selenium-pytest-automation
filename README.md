# Selenium Pytest Web Automation Framework

一个基于 Python、Selenium 和 pytest 搭建的 Web UI 自动化测试项目。

项目采用 Page Object Model（POM）设计思想，对页面操作、测试数据、配置、日志、测试用例和报告进行分层管理。

## 技术栈

- Python
- Selenium
- pytest
- pytest-html
- Page Object Model
- JSON 数据驱动
- Logging
- 显式等待 WebDriverWait

## 项目结构

```text
WelcomeScreen/
├── config/
│   └── settings.py
├── data/
│   └── web_form_data.json
├── pages/
│   ├── base_page.py
│   └── web_form_page.py
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
│   └── test_web_form.py
├── utils/
│   └── logger.py
├── logs/
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md