import urllib2
from bs4 import  BeautifulSoup

url= urllib2.urlopen('http://www.mysmartprice.com/mobile/motorola-moto-g-turbo-edition-msp8936')
soup=BeautifulSoup(url.read())

length=len(soup.findAll(attrs={"class":"store_pricetable"}))
if length>0:
 fetched=soup.findAll(attrs={"class":"store_pricetable"});
else:
 fetched=soup.findAll(attrs={"class":"prc-tbl-row"});

print "started babay"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "\n"
print fetched
