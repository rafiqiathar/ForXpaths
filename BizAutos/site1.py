#BizAutos site1
from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
url = 'http://www.lrlv.com/detail-2013-land_rover-lr2-awd_4dr-used-10523272.html'
request = urllib2.Request(url)
rawPage = urllib2.urlopen(request)
read = rawPage.read()
#print read
tree = etree.HTML(read)
title = tree.xpath("//div[@class='middleModelAndDescTop']/text()")
print 'Title=',title

interiorColor = tree.xpath("//*[@id='vehicleinfodesc']/div[22]/text()")
print 'interiorColor=', interiorColor

exteriorColor = tree.xpath("//*[@id='vehicleinfodesc']/div[18]/text()")
print 'exteriorColor =', exteriorColor

engine = tree.xpath("//*[@id='vehicleinfodesc']/div[5]/text()")
print 'engine =', engine

vin = tree.xpath("//*/div/div[@class='mgb5']/text()[2]")
print 'vin=', vin

price = tree.xpath("//div[@itemprop='price']//span/text()")
print 'price =', price.tostring()

mileage = tree.xpath("//*[@id='vehicleinfodesc']/div[11]/text()")
print 'mileage =', mileage

transmission = tree.xpath("//*[@id='vehicleinfodesc']/div[8]/text()")
print 'transmission =', transmission

dealerName = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerDealershipName']/text()")
print 'dealerName =', dealerName

dealerPhone = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerAddressPhone']/text()")
print 'dealerPhone =', dealerPhone

dealerAddress = tree.xpath("//div[@class='bannerWrapper']/div[@class='bannerAddressPhone']/span[1]/text()")
print 'dealerAddress =', dealerAddress

condition = tree.xpath("//*[@id='vehicleinfodesc']/div[2]/text()")
print 'condition =', condition

mpgCity = tree.xpath("//div[@class='CityMPG floatLeft']/div/text()")
print 'mpgCity =', mpgCity

mpgHighway = tree.xpath("//div[@class='HwyMPG floatLeft']/div/text()")
print 'mpgHighway =', mpgHighway

for imgg in tree.xpath("//div[@class='bottomListCont']"):
    t = imgg.xpath('//span/a/img/@src')
    print "Images On Page::::", t
