from getUrl import getUrl
import os
import urllib
from datetime import date

def download():
	url = getUrl()
	print url
	os.system('wget ' + str(url) + " -O " + str(os.getcwd()) + "/wallpapers/wallpaper" + str(date.today()) + ".jpg")
