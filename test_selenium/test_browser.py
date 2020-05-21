from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_selenium.test_hogwarts import TestHogwarts


class TestBrowser(TestHogwarts):
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    # def wait(self, timeout, method):
    #     WebDriverWait(self.driver, timeout).until(method)
    #
    # def test_hogwarts(self):
    #     self.driver.find_element(By.LINK_TEXT, '社团').click()
    #     self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
    #     self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()
    #
    # def test_mtsc2020(self):
    #     self.driver.get("https://testerhome.com/topics/21805")
    #     self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
    #     print(self.driver.window_handles)
    #     self.wait(10, lambda x: len(self.driver.window_handles) > 1)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     self.driver.find_element(By.LINK_TEXT, '演讲申请').click()
    #
    # def test_js(self):
    #     for code in ["return document.title", 'return document.querySelector(".active").className']:
    #         result = self.driver.execute_script()
    #         print(result)
    #
    # def teardown_method(self):
    #     sleep(5)
    #     self.driver.quit()
