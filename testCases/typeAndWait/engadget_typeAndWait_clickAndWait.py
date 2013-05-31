from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class EngadgetTypeAndWaitClickAndWait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.engadget.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_engadget_type_and_wait_click_and_wait(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//li[2]/a/span").click()
        driver.find_element_by_xpath("//a[contains(text(),'Features')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Reviews')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'News')]").click()
        driver.find_element_by_xpath("//input").clear()
        driver.find_element_by_xpath("//input").send_keys("test search")
        driver.find_element_by_xpath("//a[contains(text(),'Topics')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Buyers Guides')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Engadget')]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
