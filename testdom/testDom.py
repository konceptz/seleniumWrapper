import sys, re
from xml.dom.minidom import parse, parseString
from lxml import etree as ET
from bs4 import BeautifulSoup as bs
from lxml import etree



def main():


	#root = etree.fromstring(your_text)
	#print root.xpath("//link[contains(text(), 'rel')]/following-sibling::td/a/@href")[0]


	soup = bs(open("ads.html"))

	#find xpath of all text
	#file_obj = open("ads.html", 'r')
	#dom = parseString(file_obj)
	#build_text_list = ET.XPath("//text()")
	#tests = build_text_list(dom)	
	#remove blank links
	#cleaned = filter(lambda x: not re.match(r'^\s*$', x), tests)
	#for t in cleaned:
	#	print t

	#finds the href
	#pattern = re.compile(r'href=["|\'](?!#)(.+?)["\']');
	#base = pattern.findall(str(soup.link))
	#base = str(base)[2:-2]
	#print (base)
	#print soup.find_all('td')

	for link in soup.find_all('link'):
		print(link.get('href'))

	lst = []
	for string in soup.stripped_strings:
	#	lst.append(repr(string))
		lst.append(string)

	for x in lst:
		print x

main()
