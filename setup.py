import os

X = raw_input("This will install pip and beauiful soup.Do you want to continue? (Y/N): ")
if X.lower() == 'y':
	os.system("wget 'https://bootstrap.pypa.io/get-pip.py'")
	os.system("sudo python get-pip.py")
	os.system("sudo pip install beautifulsoup4")
	os.system("echo 'To use, cd to the directory with all the code. Use \'python setWallpaper.py\' in terminal to run'")
