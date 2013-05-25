from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait 
import time
 
sut="http://internetretailer.com"
to_be_scraped=[]
scraped=[]
 
#list of wildcards to ignore in URL pattern.
ignored = ["ignore_me", "not_important_url_prefix"] 
log = open('crawler_log.txt', 'w')
 
#I require a specific firefox profile, you may not.
#firefox_profile = "/pathtofirefoxprofile"
 
def uniqify(seq):
  # uniqifies a list.  Not order preserving
  keys = {}
  for e in seq:
    keys[e] = 1
  return keys.keys()
 
def getlinks(site):
  print "Testing %s\n" % (site)
  driver.get(site)
  print "  driver.get successful\n"
  elements = driver.find_elements_by_xpath("//a")
  print "  driver.find_elements_by_xpath successful\n"
  links = []
  for link in elements:
    try:
      if str(link.get_attribute("href"))[0:4] == "http":
        links.append(str(link.get_attribute("href")))
    except StaleElementReferenceException:
      log.write("Stale element reference found!\n")
      log.flush()
  links = uniqify(links)
  return links
 
def testlinks(links):
  badlinks = []
  for link in links:
    # I am testing for the $ character.  You can add more tests here.
    if '$' in link:
      badlinks.append(link)
  return badlinks
 
def ignore(link):
  for pattern in ignored:
    if pattern in link:
      return True
 
def scraper(site):
  links = getlinks(site)
  scraped.append(site)
  badlinks = testlinks(links)
  if badlinks:
    for link in badlinks:
      print "* Bad link on \"%s\" detected: \"%s\"" % (site, link)
      log.write("* Bad link on \"%s\" detected: \"%s\"" % (site, link))
      links.remove(link)
  log.write('Done scraping %s\n' % (site))
  log.flush()
  return links
 
def crawler():
  while to_be_scraped:
    site = to_be_scraped.pop(0)
    links = scraper(site)
    for link in links:
      if not link[0:(len(sut))] == sut:
        print "%s not at sut" % (link)
        continue
      elif link in scraped:
        print "%s has already been scraped" % (link)
        continue
      elif link in to_be_scraped:
        print "%s is already on the queue" % (link)
        continue
      elif ignore(link):
        print "%s is being ignored" % (link)
        continue
      else:
        print "adding %s to the queue" % (link)
        to_be_scraped.append(link)
 
to_be_scraped.append(sut)
#driver = webdriver.Firefox(webdriver.firefox.firefox_profile.FirefoxProfile(firefox_profile))
driver = webdriver.Firefox()
crawler()
log.close()