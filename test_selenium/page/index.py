from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    # def __init__(self, driver=None):
    #     if driver is None:
    #         self.driver = webdriver.Chrome()
    #         self.driver.implicitly_wait(3)
    #         self.driver.get("https://work.weixin.qq.com/")
    #     else:
    #         self.driver = driver

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        return Register(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业登录").click()
        return Login(self._driver)
