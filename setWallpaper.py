from download import download
import os
import time

download()
time.sleep(2)
os.system('gsettings set org.gnome.desktop.background picture-uri file://' + str(os.path.realpath('wallpaper.jpg')))
