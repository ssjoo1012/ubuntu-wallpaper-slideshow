import os
import time
import threading

path = '/home/ssj/Pictures/wallpaper'
file_list = os.listdir(path)
cnt=0

def switch_wallpaper():
	global cnt
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/ssj/Pictures/wallpaper/"+file_list[cnt])
	if cnt>=len(file_list)-1:
		cnt = 0
	else:
		cnt += 1
	threading.Timer(60*15,switch_wallpaper).start()

switch_wallpaper()
