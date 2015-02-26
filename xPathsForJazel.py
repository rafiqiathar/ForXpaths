# Check Xpath Against url"

from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
#url = 'http://www.primehondacars.com/car/330414/2005_Scion_xA_Base?vdp=2&utm_expid=97177927-0.CjwErbjmTuWaRQA_IO42ew.1&lpid=49'
#url = 'http://www.galpin.com/car/327220/2003_Mazda_Mazda6_i'
#url = 'http://www.galpinsubaru.com/car/303023/2005_Dodge_Caravan_SE?lpid=199'
#
url = 'http://www.hondaofdecatur.com/car/315990/2000_Honda_Accord_Sdn_LX'
request = urllib2.Request(url)
rawPage = urllib2.urlopen(request)
read = rawPage.read()
#print read
tree = etree.HTML(read)
#//*[@id="content"]/div/article/div[1]/div[1]/div/h1
print url
title = tree.xpath("//div[@class='vehicle-title']/h1/text() | //h1[@class='title-zone hide-for-small']/text()")
print 'Title =', title

interiorColor = tree.xpath("//div[contains(text(), 'Int. Color:')]//following-sibling::*[1]/text()")
print 'interiorColor=', interiorColor

exteriorColor = tree.xpath("//*[contains(text(), 'Ext. Color:')]//following-sibling::*[1]/text()")
print 'exteriorColor =', exteriorColor

engine = tree.xpath("//*[contains(text(), 'Engine:')]//following-sibling::*[1]/text()")
print 'engine =', engine

vin = tree.xpath("//*[contains(text(), 'VIN:')]//following-sibling::*[1]/text()")
print 'vin=', vin

price = tree.xpath("//td[@class='pricing-value pricing2']/text() | //span[@class='pricing-value no-haggle']/text()")
print 'price =', price

mileage = tree.xpath("//p//*[contains(text(), 'Mileage:')]//following-sibling::*[1]/text() \
                            |//*[contains(text(), 'Mileage:')]//following-sibling::*[1]/text()")
print 'mileage =', mileage
# //a/bb[text()="zz"]/following-sibling::cc[1]/text()
transmission = tree.xpath("//*[contains(text(), 'Transmission:')]//following-sibling::*[1]/text()")
print 'transmission =', transmission
#dealerName = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerDealershipName']/text()")
#print 'dealerName =', dealerName

dealerName = tree.xpath("//*[contains(text(), 'Located at:')]//following-sibling::*[1]/text()\
                        |//*[contains(text(), 'Located at:')]//following-sibling::*[2]/text()")
print 'dealerName =', dealerName

dealerPhone = tree.xpath("//span[@class='value']//span[@class='dynamic-phone-number']/text()\
                            | //div[@class='phone']/text()")
print 'dealerPhone =', dealerPhone

dealerAddress = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerAddressPhone']/span[1]/text()\
| //div[@class='dealership_name']/span/text() |//span[@class='address']/text()")

if len(dealerAddress)>1:
    dealerAddress = dealerName.pop()
print 'dealerAddress =', dealerAddress

condition = tree.xpath("//div[text()='Condition:']//following-sibling::*[1]/text()")
print 'condition =', condition

mpgCity = tree.xpath("//td[@class='mpg-city']/div/span[@class='mpg-value']/text()")
print 'mpgCity =', mpgCity

mpgHighway = tree.xpath("//td[@class='mpg-hwy']/div/span[@class='mpg-value']/text()")
print 'mpgHighway =', mpgHighway

features = tree.xpath("//div[@class='tech-specs-zone']/*//text()\
                         |//div[@class='tech-specs']//div[@class='panes']/*//text()")
print 'Features1 =', features

img = tree.xpath("//img[@class='gallery-active-image']/@src")
print 'ImageLink =', img

#img = tree.xpath("//a[@class='large-image-link']//img[@class='gallery-active-image']//@src")
#print 'ImageLink =', img

#for f in features:
#    print "Featuer +++++++++++++   ",f
#features = tree.xpath("//td[@class='BottomWideColumn2']//div/text()")
##print 'Features2 =', features
#for f in features:
#    print f

for imgs in tree.xpath("//div[@class='thumbnail-photo']"):
    t = imgs.xpath('//img/@data-baselink')
print "Images On Page::::", t



#features = tree.xpath("//td[@class='BottomWideColumn3']//div/text()")
##print 'Features3 =', features
#for f in features:
#    print f

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


