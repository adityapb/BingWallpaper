from download import download
import os

download()
os.system('gsettings set org.gnome.desktop.background picture-uri file://' + str(os.path.realpath('wallpaper.jpg')))
