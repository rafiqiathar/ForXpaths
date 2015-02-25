#Jazel site1
from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
url = 'http://www.primehondacars.com/car/330414/2005_Scion_xA_Base?lpid=49'
request = urllib2.Request(url)
rawPage = urllib2.urlopen(request)
read = rawPage.read()
#print read
tree = etree.HTML(read)
