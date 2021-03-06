#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import unittest
import time
import re
import sys

BASE = ''
TARGETS = []
VALUES = []
ACTIONS = []
EXECUTABLES = []


def main():

    #Extract pre-converted commands, 
    parseXmlScript()
    #init webdriver
    initWebDriver()
    #convert the actions into webdriver commands
    convertActionsToWebDriver()
    #actually run the executables
    runExecutables()
    #output the 
    fileOutput()

    

    # gets the base address

    for link in soup.find_all('link'):
        base_url = link.get('href')

    driver.get(base_url)
    commandlist = []
    for string in soup.stripped_strings:
        commandlist.append(string)

    passed = []
    failed = []
    results = []
    # gets all the commands to run
    #driver.find_element(by=By.XPATH, value="//object/embed").click()
    #driver.refresh()
    run_this = toRun(commandlist)
    
    for x in run_this:
        try:
            driver.implicitly_wait(10)
            print ("executing command : " + x)
            exec(x)
            results.append('[passed] ' +x)
            passed.append(x)
        except: 
            results.append('[failed] ' + x)
            failed.append(x)

    # code = 'driver.'+commandlist[6]+''
    # print commandlist[6]

    print ('\n\n\n')
    for x in results:
        print x
    #writefile(passed, failed)

def parseXmlScript():
    global BASE
    file_input = sys.argv[1]
    soup = bs(open(file_input))
    
    #extract base directory
    for link in soup.find_all('link'):
        #this well formed XML will only have 1 return
        BASE = link.get('href')

    #extract out targets/values/actions from soup
    triples(soup)


def initWebDriver():
    #init for firefox at this time
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)

def convertActionsToWebDriver():
    #actually run the executables

def runExecutables():
    
def passfileOutput():


def triples(soup):
    global ACTIONS
    global TARGETS
    global VALUES

    all_tds = []
    for string in soup.find_all('td'):
        all_tds.append(string)

    all_tds.pop(0)
   
    while all_tds:
        commands.append(all_tds.pop(0))
        TARGETS.append(all_tds.pop(0))
        actions.append(all_tds.pop(0))

def toRun(commands):
    converted_run_list = []
    commandSoup = bs(open('IDE_to_Python.xml'))
    ide = []
    py = []
    TARGETS = []
	
    commands = clean_commands(commands)
 
    for x in commands:
	if '/' in x:
	   TARGETS.append(x)
    # create a list of all commands in IDE and their Python Equivalents

    for link in commandSoup.find_all('commands'):
        ide.append(link.get('ide'))
        py.append(link.get('python'))

    # get a list of converted commands from IDE to Python

    for torun in commands:
        if torun in ide:
            converted_run_list.append(py[ide.index(torun)])
    
    #print (len(TARGETS))
    #print (len(converted_run_list))
    """
    for x in TARGETS:
        print x
    for x in converted_run_list:
        print x
    # get a list of all the TARGETS from commandlist
    """
    final_commands_to_exec= []
    noXpath = getNoParamCommands()
    i=0
    j=0
    
    """
    This is where we need to decide how to handle incoming commands and translate them.
    We should check the XML conversion list and enter a method to return a string.
    """
    for driver_commands in converted_run_list:
        if driver_commands in noXpath:     
            final_commands_to_exec.append('driver.'+converted_run_list[i]+'()')
        else:
            #post click needed.  Let's convert this string into a list like this:
            #if driver_commands in list_of_post_click_needed:

            #sending our command and xpath to be processed into needed command.
            final_commands_to_exec.append(convert_commands(converted_run_list[i], TARGETS[j])
            """
            if 'clickAndWait' in driver_commands: 
                final_commands_to_exec.append('driver.'+ converted_run_list[i] + '(by=By.XPATH, value=\"' + TARGETS[j]+ '\").click()') 
            #still checking against the list for other commands
            else:
                final_commands_to_exec.append('driver.'+ converted_run_list[i] + '(by=By.XPATH, value=\"' + TARGETS[j]+ '\")') 
            """
            j=j+1

        i=i+1
        



    for x in final_commands_to_exec:
        print x
    return final_commands_to_exec

def getNoParamCommands():
    npc = []
    npc.append('back')
    npc.append('delete_all_cookies')
    npc.append('forward')
    npc.append('get_cookies')
    npc.append('is_onlnie')
    npc.append('refresh')
    npc.append('close')
    return npc

def clean_commands(commands):
    #Remove the first 5 items of unneeded commands
    commands.pop(0)
    commands.pop(0)
    commands.pop(0)
    commands.pop(0)
    commands.pop(0)

    return commands


  

"""
def writefile(passed, failed):
    E = lxml.builder.ElementMaker()
    root = E.root
    Doc = E.Doc
    FIELD1 = E.status
    FIELD2 = E.command
    output = ROOT(FIELD1())
    for line in passed:




    now = datetime.datetime.now()
    time_str = str(now.strftime("%Y-%m-%d-%H-%M"))
    timefilename = "WebDriver-"
    timefilename+=time_str
    timefilename = timefilename+'.xml'
"""
   


main()
