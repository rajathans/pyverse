#!/usr/bin/env python

import click
import requests
from bs4 import BeautifulSoup as Soup
import lxml.etree

@click.command()
@click.option('--s', default=0, help='Word synonyms.')
@click.option('--w', prompt='The word',
              help='The word to get the definition of.')
def hello(s, w):
	xml = requests.get("http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/"+ w +"?key=c9e15b42-3a7c-46d8-aeca-6ee6d9f9ab88").content
	k =  open("test.xml", "wb")
	k.write(xml)
	k.close()
	#yoyo

	doc = lxml.etree.parse('test.xml')
	count = int(doc.xpath('count(//entry)'))

	with open("test.xml", "r") as f:
	    target_xml = f.read()

	print "Found", count, "related definitions"
	print
	# create a `Soup` object
	soup = Soup(target_xml, "xml")   
	for d in soup.find_all('entry'):
		print (d.term.hw.text).encode('utf8'), str(d.fl.text).upper(), str(d.sens.mc.text)
		if s==1:
			print "synonyms :", d.sens.syn.text
		print

if __name__ == '__main__':
    hello()