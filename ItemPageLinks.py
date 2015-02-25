#script for extracting links for Item pages
from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
url = 'http://www.lrlv.com/used-cars/'
request = urllib2.Request(url)
rawPage = urllib2.urlopen(request)
read = rawPage.read()
#print read
tree = etree.HTML(read)

for imgg in tree.xpath("//div"):
    t = imgg.xpath("//a[@class='fBold title fs20']/@href")
for l in t:
    print "Link for Vehicle page ", l
