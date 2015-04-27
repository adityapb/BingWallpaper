import urllib
from bs4 import BeautifulSoup

def getUrl():
	base = 'http://www.bing.com'
	page = urllib.urlopen(base)
	obj = BeautifulSoup(page)
	for script in obj.find_all('script'):
		if str(script).find('.jpg') != -1:
			img_scrpt = str(script)
	end = img_scrpt.find('.jpg') + 4
	start = img_scrpt[:end].rfind("'") + 1
	if img_scrpt[start:end].find('www') < 0:
		return base + img_scrpt[start:end]
	return img_scrpt[start:end]
