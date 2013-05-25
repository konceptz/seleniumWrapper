"""
from selenium import webdriver

#from selenium import selenium
#selenium = selenium("localhost", 4444, "*firefox", "http://google.com")
#selenium.start()

driver = webdriver.Firefox()



if __name__ == "__main__":
    main()
"""

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.internetretailer.com")
assert "Industry Strategies" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("selenium")
#elem.send_keys(Keys.RETURN)
assert "Google" in driver.title
driver.close()
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Google", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()