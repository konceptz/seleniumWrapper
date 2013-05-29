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


def main():

    # setUp(file_input)

    file_input = sys.argv[1]
    soup = bs(open(file_input))

    driver = webdriver.Firefox()
    # not using chrome or ie right now
    driver.implicitly_wait(30)

    # gets the base address

    for link in soup.find_all('link'):
        base_url = link.get('href')

    driver.get(base_url)
    commandlist = []
    for string in soup.stripped_strings:
        commandlist.append(string)

    # gets all the commands to run

    run_this = toRun(commandlist)
    
    for x in run_this:
        try:
            print ("executing command : " + x)
            exec(x)
            print ("found it %s" % x)
        except: print("failed")

    # code = 'driver.'+commandlist[6]+''
    # print commandlist[6]

def toRun(commands):
    converted_run_list = []
    commandSoup = bs(open('IDE_to_Python.xml'))
    ide = []
    py = []
    xpaths = []
	
   # parse the list of commands into a list and remove the first 5
    commands.pop(0)
    commands.pop(0)
    commands.pop(0)
    commands.pop(0)
    commands.pop(0)
 
    for x in commands:
	if '/' in x:
	   xpaths.append(x)
    # create a list of all commands in IDE and their Python Equivalents

    for link in commandSoup.find_all('commands'):
        ide.append(link.get('ide'))
        py.append(link.get('python'))

    # get a list of converted commands from IDE to Python

    for torun in commands:
        if torun in ide:
            converted_run_list.append(py[ide.index(torun)])
    
    #print (len(xpaths))
    #print (len(converted_run_list))
    """
    for x in xpaths:
        print x
    for x in converted_run_list:
        print x
    # get a list of all the xpaths from commandlist
    """
    final_commands_to_exec= []
    npc = getNoParamCommands()
    i=0
    j=0
    for driver_commands in converted_run_list:
        if driver_commands in npc:     
            final_commands_to_exec.append('driver.'+converted_run_list[i]+'()')
        else:
            final_commands_to_exec.append('driver.'+ converted_run_list[i] + '(by=XPATH value=\"' + xpaths[j]+ '\")') 
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

main()
