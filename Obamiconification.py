#Libraries
from Myro import *
from sys import *
from time import *
from random import *


#define colors as variables here
darkBlue = makeColor(5,5,5)

Red = makeColor(200, 0, 0)

Blue = makeColor(205,180,0)

Yellow = makeColor(200, 160, 0)

#Code for receiving the picture
picture = makePicture(pickAFile())

#Storing the pixels of trhe picture into variables

pic=getPixels(picture)

#Code for changing the colors based on each pixel
for pixel in pic:
    if getGray(pixel)>180:
        setColor(pixel,Yellow)
    elif getGray(pixel)>120:
        setColor(pixel,Blue)
    elif getGray(pixel)>60:
        setColor(pixel,Red)
    elif getGray(pixel)<60:
        setColor(pixel,darkBlue)

                                             
show(picture)
savePicture(picture, "newEditedPic.png") 