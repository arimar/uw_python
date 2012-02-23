import urllib2
from BeautifulSoup import BeautifulSoup

proxy = urllib2.ProxyHandler({'http' : '<Your proxy here>'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

page = urllib2.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=234')
soup = BeautifulSoup(page)

for row in soup('table', {'class' : 'spad'})[0].tbody('tr'): 
    tds = row('td') 
    print tds[0].string, ' Sunrise: ', tds[1].string, ' Sunset: ', tds[2].string
    # will print date, sunrise, and sunset
