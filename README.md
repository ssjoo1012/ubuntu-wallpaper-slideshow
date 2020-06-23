# ubuntu-wallpaper-slideshow
This changes the wallpaper with pictures inside your own directory every specified time.

## usage
1. Modify the image_path to the directory that contains the image files you want to use.
2. If you want to change the background image fastly or slowly, modify change_term. The default is 15 minutes.
3. Add this to .profile 

    $(which python) YOUR_PATH/switch_wallpaper.py &

4. This file works with python3.8 , ubuntu 20.04 LTS.
