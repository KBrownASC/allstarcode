from time import*
from random import*

x = 250
r = 1
c = 1
y = 605
directionRight = .5
amovex = 300
amovey = 70
bullet = False

def setup():
    global r
    global c

    frameRate(60)
    background(1)
    size(600,600)
    

    
def draw():
    
    alien=[[0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]
    r = 1
    global x
    global y
    global bulletX
    global amovex
    global directionRight
    global amovey

#Bullet
    background(1)
    global bullet
    if bullet == True:
        fill(0,255,80)
        noStroke
        rect(bulletX + 30,y,10,10)
    if y != 605:
        y = y - 7
        if y <= 0:
            y = 605
    if y == 605 and keyPressed and key == ' ': 
        bullet = True
        bulletX = x
        y = y - 1

#Player
    fill(0,255,80)
    noStroke
    rect(x,570, 70,40)
    if keyPressed and key == 'a':
        x=x-10   
    if keyPressed and key == 'd':
        x=x+10
        
        
        

    
#AlienCharacter
    
    
    for y1 in [0,1,2,3,4,5]:
        for x1 in [0,1,2,3,4,5]:
            alienPos = amovex + x1*50
            if alien[y1][x1] == 0:
                fill(200,120,0)
                ellipse(alienPos,amovey + y1 *50,25,25)
                amovex = amovex - directionRight

            elif alien[y1][x1] == 1:
                print(1)

    if amovex <= 0:
        directionRight = directionRight * -1
        amovey = amovey + 5
    if amovex >= 450:
        directionRight = directionRight * -1
        amovey = amovey + 5
    if amovey >= 450:
        amovey = 500
        background(255,50,50)
        fill(1)
        textSize(80)
        text("You lose", 100,300)          
    
        