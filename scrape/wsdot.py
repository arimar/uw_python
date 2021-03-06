import urllib2
from BeautifulSoup import BeautifulSoup

page_north = urllib2.urlopen('http://www.wsdot.wa.gov/small/Seattle/TravelTimes/nbtimes.aspx')
page_south = urllib2.urlopen('http://www.wsdot.wa.gov/small/Seattle/TravelTimes/sbtimes.aspx')

soup = BeautifulSoup(page_north)

print "*****************************************************************"
print "                          HEADING NORTH"
print "*****************************************************************"

try:
    for row in soup('tr', {'class' : 'tablerow'}):
    	tds = row('td')
    	#print [tds[0].findAll(text=True).pop(i) for i in range(len(tds[0].findAll(text=True)))]
    	for i in range(len(tds[0].findAll(text=True))):
        	print tds[0].findAll(text=True).pop(i),
    		print
    	print "    Average:  %s minutes, " % tds[2].text,
    	print "Current:  %s minutes" % tds[3].text
    	print

    for row in soup('tr', {'class' : 'tablerowalt'}):
    	tds = row('td')
    	#print [tds[0].findAll(text=True).pop(i) for i in range(len(tds[0].findAll(text=True)))]
    	for i in range(len(tds[0].findAll(text=True))):
        	print tds[0].findAll(text=True).pop(i),
    	print
    	print "    Average:  %s minutes, " % tds[2].text,
    	print "Current:  %s minutes" % tds[3].text
    	print

except IndexError:
    pass

soup = BeautifulSoup(page_south)

print "*****************************************************************"
print "                          HEADING SOUTH"
print "*****************************************************************"

try:
    for row in soup('tr', {'class' : 'tablerow'}):
    	tds = row('td')
    	#print [tds[0].findAll(text=True).pop(i) for i in range(len(tds[0].findAll(text=True)))]
    	for i in range(len(tds[0].findAll(text=True))):
        	print tds[0].findAll(text=True).pop(i),
    	print
    	print "    Average:  %s minutes, " % tds[2].text,
    	print "Current:  %s minutes" % tds[3].text
    	print

    for row in soup('tr', {'class' : 'tablerowalt'}):
    	tds = row('td')
    	#print [tds[0].findAll(text=True).pop(i) for i in range(len(tds[0].findAll(text=True)))]
    	for i in range(len(tds[0].findAll(text=True))):
        	print tds[0].findAll(text=True).pop(i),
    	print
    	print "    Average:  %s minutes, " % tds[2].text,
    	print "Current:  %s minutes" % tds[3].text
    	print

except IndexError:
    pass
