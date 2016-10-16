import re
import requests
from bs4 import BeautifulSoup
from MangaParkLinkGrabber import *

url2 = "http://mangapark.me/manga/one-piece"
url2Parts = url2.split("/")
print (url2Parts)
mangaUrl = "/"+url2Parts[3]+"/"+url2Parts[4]+"/"
thePageContent = getPageContent(url2)
allLinks = thePageContent.find_all("a")
for link1 in allLinks:
    tempLink1 = str(link1.get("href"))
    if mangaUrl in tempLink1 :
        print (url2Parts[0]+"//"+url2Parts[2]+tempLink1)
