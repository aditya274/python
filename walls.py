from urllib import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
import random
import datetime
import os

random.seed(datetime.datetime.now())

def getDownloadLink(title):
	if not os.path.exists(title):
		os
	url = "https://wall.alphacoders.com/search.php?search=" +title
	html = urlopen(url)
	bsObj = BeautifulSoup(html, "html.parser")
	divs = bsObj.findAll('div', {'class':'boxgrid'})
	for text in divs:
		downloads = text.findAll('a')
		for download in downloads:
			images = download.findAll('img')
			for image in images:
				print image['src']
				if image['src'][-3] == 'j':
					ext = ".jpg"
				else: ext = ".png"
				print ext
				urlretrieve(image['src'], "walls/alphacoders/" +str(random.randint(0, 1000))+ ext)

getDownloadLink(raw_input("Enter wallpaper category: "))