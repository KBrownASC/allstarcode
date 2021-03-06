from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Myro Colors", width, height, Color("purple"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("brown"))
sim.addWall((10, 10), (20, 490), Color("brown"))
sim.addWall((480, 10), (490, 490), Color("brown"))
sim.addWall((10, 480), (490, 490), Color("brown"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 200 and getGreen(pixel) == 0 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel)== 0 and getGreen(pixel) > 90 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) == 0 and getGreen(pixel) == 0 and getBlue(pixel) > 200):
          
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 180 and getGreen(pixel) > 180 and getBlue(pixel) == 0):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################
red=1
green=2
blue=3
yellow=4

blueValue=0
greenValue=0
redValue=0
yellowValue=0

while blueValue<1:
    motors(1,-1,.5)
    pic= takePicture()
    getWidth(pic)
    show(pic)
    if findColorSpot(pic,3):
        motors(1,-1,.75)
        forward(1,3)
        move=0
        while move<2:
            forward(2,2)
            move=move+2
        blueValue=blueValue+1
        backward(1,1)

sim.setPose(0, width/2, height/2, 0)


while greenValue<1:
    motors(1,-1,.5)
    pic= takePicture()
    getWidth(pic)
    show(pic)
    if findColorSpot(pic,2):
        motors(1,-1,1)
        forward(1,3)
        move=0
        while move<2:
            forward(2,2)
            move=move+2
        greenValue=greenValue+1
        backward(1,1)

sim.setPose(0, width/2, height/2, 0)

while redValue<1:
    motors(1,-1,1)
    pic= takePicture()
    getWidth(pic)
    show(pic)
    if findColorSpot(pic,1):
        motors(1,-1,.5)
        forward(1,3)
        move=0
        while move<2:
            forward(2,2)
            move=move+2
        redValue=redValue+1
        backward(1,1)

sim.setPose(0, width/2, height/2, 0)

while yellowValue<1:
    motors(1,-1,1)
    pic= takePicture()
    getWidth(pic)
    show(pic)
    if findColorSpot(pic,4):
        motors(1,-1,.5)
        forward(1,3)
        move=0
        while move<2:
            forward(2,2)
            move=move+2
        yellowValue=yellowValue+1
        backward(1,1)

sim.setPose(0, width/2, height/2, 0)
print("Good Job!")
