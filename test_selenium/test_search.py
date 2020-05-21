import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        pass
        # self.driver.quit()

    def test_search(self):
        self.driver.get("https://testerhome.com/")
        self.driver.set_window_size(1440, 877)
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("appium")
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
