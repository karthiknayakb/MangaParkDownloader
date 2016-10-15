import re
import requests
from bs4 import BeautifulSoup

##Returns the BeautifulSoup object
def getPageContent(url):
    pageUrl = requests.get(url)
    pageContent = BeautifulSoup(pageUrl.content,"html.parser")
    return pageContent

##Returns the string of mangaName from the url
def getMangaName(url):
    urlPart = url.split("/")
    mangaName = urlPart[4]+'/'+urlPart[5]+'/'+urlPart[6]
    return mangaName

##returns all the links chapter pages
def getPageList(pageContent1,mangaName):
    links = pageContent1.find_all("a")
    pageLinks = []
    for chapLink in links:
        tempLink = str(chapLink.get("href"))
        if mangaName in tempLink:
            pageLinks.append("http://mangapark.me"+tempLink)
    pageLinks = list(set(pageLinks))
    return pageLinks;

##returns the image link for a chapter page url
def getImageLink(pageContent2):
    imgs = pageContent2.find_all("img")
    for imgLink in imgs:
        tempImgLink = imgLink.get("src")
        if "logo-mini.png" not in tempImgLink:
            return tempImgLink

##for human sorting : http://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
##have absolutely no idea how it works. (let me know if you understand!!)
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

##Returns a chapter's all image urls
def getChapterImgUrls(linksList):
    imageUrls = []
    for link in linksList:
        tempImgLink = getImageLink(getPageContent(link))
        imageUrls.append(tempImgLink)
    return imageUrls

##Main function to run!
##need to imput the manga chapter link (The first link)
def initCrawl(url):
    pageContent = getPageContent(url)
    mangaName = getMangaName(url)
    pages = natural_sort(getPageList(pageContent,mangaName))
    return pages

url1 = "http://mangapark.me/manga/one-piece/s3/c840/1"
pages1 = initCrawl(url1)
print ("-------------Links------------")
for link in pages1:
    print (link)
print ("-------------Images------------")
urls = getChapterImgUrls(pages1)
for url in urls:
    print (url)
