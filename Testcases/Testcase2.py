# Generated by Selenium IDE
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
    self.driver.quit()
  
  def test_testCase1(self):
    self.driver.get("http://127.0.0.1:5501/")
    self.driver.set_window_size(1440, 900)
    self.driver.find_element(By.ID, "mail").click()
    self.driver.find_element(By.ID, "mail").send_keys("johndoe@abc.com")
    self.driver.find_element(By.ID, "pass").send_keys("123456")
    self.driver.find_element(By.ID, "remember").click()
    self.driver.find_element(By.ID, "forgot").click()
    self.driver.find_element(By.ID, "btn1").click()
    self.driver.find_element(By.ID, "radio").click()
    self.driver.find_element(By.ID, "anime_title").click()
    self.driver.find_element(By.ID, "anime_title").send_keys("Slam Dunk")
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.ID, "btn2").click()
    self.driver.find_element(By.CSS_SELECTOR, ".anidetails_search_title:nth-child(1) > #anime_title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".anidetails_search_title:nth-child(1) > #anime_title").send_keys("Slam Dunk")
    self.driver.find_element(By.ID, "open").click()
    self.driver.find_element(By.ID, "anime1").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
    self.vars["image1height"] = self.driver.execute_script("return window.getComputedStyle(document.querySelector(\'#image1\')).getPropertyValue(\'height\');")
    print("{}".format(self.vars["image1height"]))

    assert(self.vars["image1height"] == "100px")
  
