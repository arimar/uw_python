"""
scrape1.py
Screen-scraping demo: open a page, find and print the first anchor element
"""

import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://block335036-6hf.blueboxgrid.com:8080/' # My thirty minute webserver
#page = urllib2.urlopen(url).read()  # now page is one big string
page = urllib2.urlopen(url)  # now page is one big string

#start = page.find('<a ')    # use string method to find first start tag
#print page[start:start+60]  # print 60 characters starting at tag

soup = BeautifulSoup(page)

for fword in soup('<a ', width="90%"):
	where, linebreak, what = fword.contents[:3]
	print where.strip()
	print what.strip()
	print
