from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from lxml import etree as ET
import unittest, time, re, sys



class SeleniumtoWebdriver(unittest.TestCase):
    def setUp(self):
        text = getText(raw_input("Filename of test Script:  testYoutube.html"))
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url_variable
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def getText(filename):
        file_obj = open(user_filename, 'r')
        dom = ET.parse(file_obj)
        build_text_list = ET.XPath("//text()")
        tests = build_text_list(dom)    
        return(filter(lambda x: not re.match(r'^\s*$', x), tests))

    def test_seleniumto_webdriver(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        asdgfhaefjklsklafj
        #loop over commands with xpaths here

        
    
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
