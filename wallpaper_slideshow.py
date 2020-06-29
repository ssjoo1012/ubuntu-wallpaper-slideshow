import os
import time
import threading

image_path = '/home/ssj/Pictures/wallpaper'
image_list = os.listdir(image_path)
image_list.sort()
image_list_index=0

change_term = 15 #minutes

def switch_wallpaper():
	global image_list_index

	check_image_list()
	os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/ssj/Pictures/wallpaper/"+image_list[image_list_index])

	image_list_index += 1
	if image_list_index>=len(image_list):
		image_list_index = 0

	threading.Timer(60*change_term,switch_wallpaper).start()

#check if user add or delete image file.
def check_image_list():
	global image_list
	global image_list_index

	image_list_temp = os.listdir(image_path)
	image_list_temp.sort()

	if image_list != image_list_temp: #add or delete image file
		image_list = image_list_temp #replace image_list
		image_list_index = 0 #restart slide show

switch_wallpaper()
