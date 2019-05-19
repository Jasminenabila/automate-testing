from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest, time, re, datetime
import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path  # python3 only
env_path = '.env'
load_dotenv(dotenv_path=env_path)
from time import sleep

class Test_Dress(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.verificationErrors = []
        self.accept_next_alert = True
  
    def test_category_dress(self):

        driver = self.driver

        get_url = os.getenv("URL")

        self.driver.get(get_url)
        time.sleep(5)
        element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//img[@class='logo img-responsive']"))
        )
        driver.fullscreen_window()

        print("Show URL Successfully")

        hover_women = driver.find_element_by_xpath("//a[@title='Women']")
        
        hover = ActionChains(driver).move_to_element(hover_women)
        hover.perform()
        time.sleep(5)
        print("success to redirect tab women")

        hover_dress = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]")
        summer = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[6]/ul[1]/li[1]/ul[1]/li[2]/ul[1]/li[3]/a[1]")
        summer.click()
        time.sleep(5)

        text_dress = driver.find_element_by_xpath("//span[@class='category-name']")
        if text_dress.text == 'Summer Dresses':
            print("success detected")
        else:
            print("not detected")

        time.sleep(3)
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    