from getUrl import getUrl
import os
import urllib

def download():
	url = getUrl()
	print url
	os.system('wget ' + str(url) + " -O wallpaper.jpg")
