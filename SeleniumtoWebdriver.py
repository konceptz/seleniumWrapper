from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import unittest, time, re, sys

BASE = ""

def main():
    #setUp(file_input)
    file_input = sys.argv[1]
    soup = bs(open(file_input))
    #driver = webdriver.Firefox()
    #not using chrome or ie right now
    #driver.implicitly_wait(30)
    
    #gets the base address    
    for link in soup.find_all('link'):
        base_url = link.get('href')
    #driver.get(base_url)
    commandlist = []
    for string in soup.stripped_strings:
        commandlist.append(string)

    #gets all the commands to run    
    toRun(commandlist)

    #code = 'driver.'+commandlist[6]+''
    #print commandlist[6]
    """
    try: 
        driver.find_element(By.XPATH, commandlist[7])
        #driver.verifyElementPresent(By.XPATH, commandlist[7])
        print True
    except NoSuchElementException, e: print False
    """

def toRun(commands):
    converted_run_list = []
    commandSoup = bs(open("IDE_to_Python.xml"))
    ide = []
    py = []
    xpaths = []

    #remove the first 4 items of list.
    del co

    #create a list of all commands in IDE and their Python Equivalents
    for link in commandSoup.find_all('commands'):
        ide.append(link.get('ide'))
        py.append(link.get('python'))

    #get a list of converted commands from IDE to Python
    
    for torun in commands:
        if torun in ide:
            print py[ide.index(torun)]

            converted_run_list.append(py[ide.index(torun)])
            xpaths.append(py[ide.index(torun) +1])

    #get a list of all the xpaths from commandlist
    


"""
    full_exec_commands = []
    for python_commands in converted_run_list:
        full_exec_commands.append("exec ")
"""
"""
def getBase():
    
def getList():

def setUp():
    soup = bs(open(file_input))
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    for link in soup.find_all('link'):
        base_url = link.get('href')
    driver.get(base_url)
""" 

main()