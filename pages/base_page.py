from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from config.settings import DEFAULT_TIMEOUT
from utils.logger import get_logger


class BasePage:
    """所有 Page Object 的基础页面类"""

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            DEFAULT_TIMEOUT
        )

        self.logger = get_logger(
            self.__class__.__name__
        )

    # =========================
    # 基础页面操作
    # =========================

    def open(self, url):
        """打开网页"""

        self.logger.info(
            f"打开页面：{url}"
        )

        self.driver.get(url)

    def input(self, locator, text):
        """清空输入框，然后输入文字"""

        self.logger.info(
            f"等待输入框可操作：{locator}"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.clear()
        element.send_keys(text)

        self.logger.info(
            f"输入完成：{locator} -> {text}"
        )

    def click(self, locator):
        """等待元素可点击，然后点击"""

        self.logger.info(
            f"等待元素可点击：{locator}"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

        self.logger.info(
            f"点击完成：{locator}"
        )

    def get_text(self, locator):
        """
        获取元素文字。

        如果页面 DOM 更新导致元素变成 stale，
        则重新定位元素并继续等待。
        """

        self.logger.info(
            f"获取元素文字：{locator}"
        )

        def read_text(driver):
            try:
                # 每一次等待循环都重新定位元素
                element = driver.find_element(
                    *locator
                )

                # 元素不可见时继续等待
                if not element.is_displayed():
                    return False

                # 获取当前最新元素的文字
                text = element.text

                # 文字暂时为空时继续等待
                if not text:
                    return False

                return text

            except StaleElementReferenceException:
                # DOM 更新导致当前元素失效
                # 返回 False，让 WebDriverWait 再次尝试
                self.logger.info(
                    f"元素已失效，重新定位：{locator}"
                )

                return False

        text = self.wait.until(
            read_text
        )

        self.logger.info(
            f"获取到文字：{text}"
        )

        return text

    def get_attribute(
        self,
        locator,
        attribute_name
    ):
        """获取元素属性"""

        self.logger.info(
            f"获取元素属性：{locator} -> {attribute_name}"
        )

        element = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        value = element.get_attribute(
            attribute_name
        )

        self.logger.info(
            f"属性值：{attribute_name} = {value}"
        )

        return value

    # =========================
    # URL
    # =========================

    def wait_for_url_contains(self, text):
        """等待 URL 包含指定内容"""

        self.logger.info(
            f"等待 URL 包含：{text}"
        )

        self.wait.until(
            EC.url_contains(text)
        )

        self.logger.info(
            f"URL 已切换：{self.driver.current_url}"
        )

    # =========================
    # 多窗口
    # =========================

    def get_current_window(self):
        """获取当前窗口句柄"""

        window = (
            self.driver.current_window_handle
        )

        self.logger.info(
            f"当前窗口：{window}"
        )

        return window

    def get_all_windows(self):
        """获取所有窗口句柄"""

        windows = (
            self.driver.window_handles
        )

        self.logger.info(
            f"当前窗口数量：{len(windows)}"
        )

        return windows

    def switch_to_window(
        self,
        window_handle
    ):
        """切换到指定窗口"""

        self.driver.switch_to.window(
            window_handle
        )

        self.logger.info(
            f"切换窗口成功：{window_handle}"
        )

    def switch_to_new_window(
        self,
        old_windows
    ):
        """等待新窗口出现并切换"""

        self.logger.info(
            "等待新窗口出现"
        )

        self.wait.until(
            EC.new_window_is_opened(
                old_windows
            )
        )

        new_windows = (
            self.driver.window_handles
        )

        for window in new_windows:

            if window not in old_windows:

                self.driver.switch_to.window(
                    window
                )

                self.logger.info(
                    f"已切换到新窗口：{window}"
                )

                return window

    # =========================
    # iframe
    # =========================

    def switch_to_frame(
        self,
        frame
    ):
        """进入 iframe"""

        self.logger.info(
            f"等待并进入 iframe：{frame}"
        )

        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                frame
            )
        )

        self.logger.info(
            "进入 iframe 成功"
        )

    def switch_to_default_content(self):
        """返回主页面"""

        self.driver.switch_to.default_content()

        self.logger.info(
            "已切回主页面"
        )

    # =========================
    # Alert
    # =========================

    def wait_for_alert(self):
        """等待 Alert 出现"""

        self.logger.info(
            "等待 Alert 出现"
        )

        return self.wait.until(
            EC.alert_is_present()
        )

    def get_alert_text(self):
        """获取 Alert 文字"""

        alert = self.wait_for_alert()

        text = alert.text

        self.logger.info(
            f"Alert 内容：{text}"
        )

        return text

    def accept_alert(self):
        """点击 Alert 确定"""

        alert = self.wait_for_alert()

        alert.accept()

        self.logger.info(
            "Alert 已点击确定"
        )

    def dismiss_alert(self):
        """点击 Alert 取消"""

        alert = self.wait_for_alert()

        alert.dismiss()

        self.logger.info(
            "Alert 已点击取消"
        )

    def input_alert(
        self,
        text
    ):
        """向 Prompt 输入文字"""

        alert = self.wait_for_alert()

        alert.send_keys(text)

        self.logger.info(
            f"Prompt 已输入：{text}"
        )