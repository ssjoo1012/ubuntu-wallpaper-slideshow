import os
import time
import threading

image_path = '/home/ssj/Pictures/wallpaper'
image_list = os.listdir(image_path)
change_term = 15 #minutes
image_list_index=0

def switch_wallpaper():
	global image_list_index

	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/ssj/Pictures/wallpaper/"+image_list[image_list_index])

	image_list_index += 1
	if image_list_index>=len(image_list)-1:
		image_list_index = 0

	threading.Timer(60*change_term,switch_wallpaper).start()

switch_wallpaper()
