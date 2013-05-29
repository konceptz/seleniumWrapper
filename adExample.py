from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class AdExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.internetretailer.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ad_example(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # live ad has object for side flash and top flash
        try: self.assertTrue(self.is_element_present(By.XPATH, "//object/embed"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='col_b']/div[2]"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//[@id='ad_module']/object"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='col_b']/div[2]/object"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [unknown command []]
        # a
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header_ad']/a/"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # flash homepgae right side
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='col_b']/div[2]/object"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # home page right text ad
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='col_b']/div[2]/a"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Vendors").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='vendor-main']/div/a"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='vendor-main']/div/object"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='vendor-directory']/div/div[2]/div/a/"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("E-Commerce Systems").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[2]/div/div[2]/div[2]/div/object"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Resource Library").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header_ad']/a/"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Shop").click()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='header_ad']/a"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        # ERROR: Caught exception [ERROR: Unsupported command [deleteAllVisibleCookies |  | ]]
        driver.refresh()
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='interstitial']/div[2]/div"))
        except AssertionError as e: self.verificationErrors.append(str(e))
    
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
