
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

class TestTestCase8():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testCase8(self):
    self.driver.get("http://127.0.0.1:5500/")
    self.driver.set_window_size(1200, 746)
    self.driver.find_element(By.ID, "mail").click()
    self.driver.find_element(By.ID, "mail").send_keys("gangey@patel.com")
    self.driver.find_element(By.ID, "pass").send_keys("papapasad s")
    self.driver.find_element(By.ID, "btn1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#animeTypes > div:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#animeTypes > div:nth-child(1)").click()
    self.driver.find_element(By.ID, "radio").click()
    self.driver.find_element(By.ID, "btn2").click()
    self.driver.find_element(By.ID, "anime1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".anidetails").click()
    self.driver.find_element(By.CSS_SELECTOR, ".anidetails_search_title:nth-child(1) > #anime_title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".anidetails_search_title:nth-child(1) > #anime_title").send_keys("dasda")
    self.driver.find_element(By.ID, "open").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
    elements = self.driver.find_elements(By.XPATH, "/html/body/div[3]/div/form/div[4]/span[1]/label")
    assert len(elements) > 0
  
