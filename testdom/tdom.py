import sys, re
from xml.dom.minidom import parse, parseString
from lxml import etree as ET
from bs4 import BeautifulSoup as bs
from lxml import etree



def main():
	#root = etree.fromstring(your_text)
	#print root.xpath("//link[contains(text(), 'rel')]/following-sibling::td/a/@href")[0]


	soup = bs(open("type.html"))
	for link in soup.find_all('link'):
		print(link.get('href'))

	#lst = []
	#for string in soup.find_all('td'):
	#	print string
	#	lst.append(string)


	#lst.pop(0)

	#for x in lst:
	#	print x

	commands = []
	xpaths = []
	actions = []

	all_tds = []
	for string in soup.find_all('td') :
		all_tds.append(string)

	#for x in lst:
	#	print x

	#all_tds = lst
	all_tds.pop(0)
	#for x in all_tds:
	#	print x

	while all_tds:
		commands.append(all_tds.pop(0))
		xpaths.append(all_tds.pop(0))
		actions.append(all_tds.pop(0))
	i=0    
	for x in commands:
		print (str(i)+ ' ' +str(x))
		i=i+1

	i=0
	for x in xpaths:
		print (str(i)+ ' ' +str(x))
		i=i+1

	i=0
	for x in actions:
		print (str(i)+ ' ' + str(x))
		i=i+1

main()