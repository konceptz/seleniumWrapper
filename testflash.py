from FlashSelenium import FlashSelenium
from selenium import selenium

url = "http://flashselenium.t35.com/colors.html"
browserType = "*firefox"

selenium = selenium("localhost", 4444, browserType, url)
selenium.start()
selenium.open(url)

flashApp = FlashSelenium(selenium, "coloredSquare")
flashApp.percent_loaded()