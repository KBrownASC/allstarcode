from time import *
from random import *


#vars
moveX= 250
moveY= 250
SpdX=0
SpdY=0
SpdX2=0
SpdY2=0
rectY=225
rectX=100
i=0
rectY2=225
def setup():
    global SpdX
    global SpdY
    background(255,0,0)
    size(500,500)
    sleep(.1)
    SpdX=randint(-10,10)
    SpdY=randint(-10,10)
    SpdX2=randint(-20,20)
    SpdY2=randint(-20,20)
    sleep(.1)
    
    
def draw():
    global moveX
    global moveY
    global rectY
    global SpdX
    global SpdY
    global SpdX2
    global i
    global rectX
    global rectY2
    
    background(255,0,0)
#Player 2        
    fill(1)
    stroke(1)
    rect(480,rectY,40,100)
    if keyPressed and key=='s':
        rectY=rectY+10
if keyPressed and key=='w':
        rectY=rectY-10
    elif moveX >= 445 and moveY >= rectY+51 and moveY >= rectY-51:
        SpdX=SpdX*-1
        SpdY=SpdY*-1
        print(i+1)
        sleep(.1)


  
    fill(181)
    stroke(180)
    ellipse(moveX,moveY,25,25)
    moveX=moveX+SpdX
    moveY=moveY+SpdY
    
    
    #if moveX >= 490
        #sleep(.01)
       #SpdX=SpdX*-1

    if moveX <= 10:
        sleep(.01)
        SpdX=SpdX*-1

    if moveY >= 490:
        sleep(.01)
        SpdY=SpdY*-1

    if moveY <= 10:
        sleep(.01)
        SpdY=SpdY*-1
        
    if moveX >= 445 and moveY >= rectY+51 and moveY >= rectY-51:
        SpdX=SpdX*-1
        SpdY=SpdY*-1
        print(i+1)
        sleep(.1)
        return(i)
    

                    
    if moveX >= 520:
        moveX=250
        moveY=250
        print("you lose")
        sleep(3)