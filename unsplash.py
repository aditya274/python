from urllib import urlopen
from urllib import urlretrieve
import random
from bs4 import BeautifulSoup
import datetime
import os

random.seed(datetime.datetime.now())
category = raw_input("Enter wallpaper search: ")
url = "https://unsplash.com/search/photos/" + category
if category == "":
	url = "https://unsplash.com/"
	category = "mainpage"
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")
directory = "walls/" +category
if not os.path.exists(directory):
	os.makedirs(directory)

for link in bsObj.findAll("a", {"class":"_1QwHQ _1l4Hh _1CBrG _1zIyn xLon9 _1Tfeo _2L6Ut _2Xklx"}):
	print "Downloading: "+link["href"]
	urlretrieve(link["href"], directory +"/"  +str(random.randint(0, 1000))+".jpg")
