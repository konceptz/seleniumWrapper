import sys, re
from xml.dom.minidom import parse, parseString
from lxml import etree as ET



def main():
	file_obj = open("youtube.html", "r")
	dom = ET.parse(file_obj)
	build_text_list = ET.XPath("//text()")
	tests = build_text_list(dom)	
	cleaned = filter(lambda x: not re.match(r'^\s*$', x), tests)
	#for t in cleaned:
	#	print t

	test_list = ET.XPath("//tags()")
	print (test_list(dom))

main()
