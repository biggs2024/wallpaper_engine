"""
Author: Kalis Sandlin
Created On: 11/03/2026
Last Modified: 11/03/2026 
Description: Utilize Python Pillow package to 
create a static background image for a custom
wallpaper

"""
# import the image class from Pillow
from PIL import Image

# Image creates a new object of RGB type with size 2560x1080 and all one color
# this case the color white
white_img = Image.new("RGB", (2560, 1080), (255, 255, 255))

# displays image
# white_img.show()

white_img.save("white_background.png")
