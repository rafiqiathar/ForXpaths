# Check Xpath Against url"

from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
#
url = 'http://www.lrlv.com/detail-2011-bmw-x5_m-used-13304123.html'
#url = 'http://www.hudsontoyota.com/detail-2009-toyota-yaris-s-used-13087468.html'
#url = 'http://www.dependablemitsubishi.com/detail-2013-chevrolet-cruze-lt-used-11006339.html'
#url = 'http://www.nielsenkia.com/detail-2008-buick-enclave-fwd_4dr_cxl-used-13161900.html'
request = urllib2.Request(url)
rawPage = urllib2.urlopen(request)
read = rawPage.read()
#print read
tree = etree.HTML(read)
#//*[@id="content"]/div/article/div[1]/div[1]/div/h1
print url
title = tree.xpath("//div[@class='middleModelAndDescTop']/text()")
print 'Title =', title

interiorColor = tree.xpath("//*[contains(text(), 'Interior Color:')]//following-sibling::*[2]/text()")
print 'interiorColor=', interiorColor

exteriorColor = tree.xpath("//*[contains(text(), 'Exterior Color:')]//following-sibling::*[2]/text()")
print 'exteriorColor =', exteriorColor

engine = tree.xpath("//*[contains(text(), 'Engine:')]//following-sibling::*[1]/text()")
print 'engine =', engine

vin = tree.xpath("//*/div/div[@class='mgb5']/text()[2]")
print 'vin=', vin

price = tree.xpath("//div[@itemprop='price']//span/text() | //div[@class='price-display-value-highlight']/span/text()")
print 'price =', price

mileage = tree.xpath("//*[contains(text(), 'Mileage:')]//following-sibling::*[1]/text()")
print 'mileage =', mileage
# //a/bb[text()="zz"]/following-sibling::cc[1]/text()
transmission = tree.xpath("//*[contains(text(), 'Transmission:')]//following-sibling::*[1]/text()")
print 'transmission =', transmission
#dealerName = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerDealershipName']/text()")
#print 'dealerName =', dealerName

dealerName = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerDealershipName']/text() \
| //div[@class='dealership_name']/text()|//div[@class='banner_name']/text()")
print 'dealerName =', dealerName

dealerPhone = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerAddressPhone']/text()\
                            | //span[@class='phone']/text()")
print 'dealerPhone =', dealerPhone

dealerAddress = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerAddressPhone']/span[1]/text()\
| //div[@class='dealership_name']/span/text() |//span[@class='address']/text()")
print 'dealerAddress =', dealerAddress

condition = tree.xpath("//div[text()='Condition:']//following-sibling::*[1]/text()")
print 'condition =', condition

mpgCity = tree.xpath("//div[@class='CityMPG floatLeft']/div/text()")
print 'mpgCity =', mpgCity

mpgHighway = tree.xpath("//div[@class='HwyMPG floatLeft']/div/text()")
print 'mpgHighway =', mpgHighway

features = tree.xpath("//td[@class='BottomWideColumn1']//div/text()")
#print 'Features1 =', features
for f in features:
    print f
features = tree.xpath("//td[@class='BottomWideColumn2']//div/text()")
#print 'Features2 =', features
for f in features:
    print f
features = tree.xpath("//td[@class='BottomWideColumn3']//div/text()")
#print 'Features3 =', features
for f in features:
    print f

#status
#make
#model
#year
#dealerLat
#dealerLon
#image
#bodyStyle
#trim
#features

#for imgg in tree.xpath("//div[@class='bottomListCont']"):
#    t = imgg.xpath('//span/a/img/@src')
#    print "Images On Page::::", t
