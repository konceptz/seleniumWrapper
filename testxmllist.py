from bs4 import BeautifulSoup as bs
import unittest, time, re, sys


ide = []
py = []

soup = bs(open("IDE_to_Python.xml"))




for link in soup.find_all('commands'):
	ide.append(link.get('ide'))
	py.append(link.get('python'))
	#com[0].append(link.get('ide'))
	#com[1].append(link.get('python'))
	

i=0
for ide_com in ide:
	print ("IDE command is : " + ide_com  + "  Matching Python command is : " + py[i])
	i=i+1
	
