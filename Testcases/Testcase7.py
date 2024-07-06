
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

class TestTestCase6():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testCase6(self):
    self.driver.get("http://127.0.0.1:5500/")
    self.driver.set_window_size(1200, 746)
    self.driver.find_element(By.CSS_SELECTOR, "#Page1 > form").click()
    self.driver.find_element(By.ID, "mail").send_keys("luffy@zoro.com")
    self.driver.find_element(By.ID, "pass").send_keys("skjdvbguysdbhv")
    self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(1)").click()
    self.driver.find_element(By.ID, "remember").click()
    self.driver.find_element(By.ID, "forgot").click()
    self.driver.find_element(By.ID, "btn1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#animeTypes > div:nth-child(2)").click()
    self.driver.find_element(By.NAME, "Senin").click()
    self.driver.find_element(By.ID, "anime_title").click()
    self.driver.find_element(By.ID, "anime_title").send_keys("gintama")
    self.driver.find_element(By.ID, "btn2").click()
    self.driver.find_element(By.ID, "anime1").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
    elements = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div/form/div[3]/div/label")
    assert len(elements) > 0
  
