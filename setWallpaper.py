from download import download
import os
from datetime import date

download()
os.system('gsettings set org.gnome.desktop.background picture-uri file://' + str(os.getcwd()) + '/wallpapers/wallpaper' + str(date.today()) + '.jpg')
