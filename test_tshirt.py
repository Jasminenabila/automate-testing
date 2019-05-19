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

class Test_Tshirt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.verificationErrors = []
        self.accept_next_alert = True
  
    def test_category_tshirt(self):

        driver = self.driver

        get_url = os.getenv("URL")

        self.driver.get(get_url)
        time.sleep(5)
        element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//img[@class='logo img-responsive']"))
        )
        driver.fullscreen_window()

        print("Show URL Successfully")

        navbar_tshirt = driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a').click()
        time.sleep(5)
        print("success page tshirt")

        text_tshirt = driver.find_element_by_xpath("//span[@class='category-name']")

        if text_tshirt.text == 'T-shirts':
            print("detected text category t-shirt")
        else:
            print("not detected")
 

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
    