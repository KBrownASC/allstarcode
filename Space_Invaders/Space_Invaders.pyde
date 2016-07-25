from time import*
from random import*

x = 250
r = 1
c = 1
y = 605
bullet = False

def setup():
    global r
    global c
    
    frameRate(60)
    background(0)
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
    background(1)    
#Alien 
    
    for y1 in [0,1,2,3,4,5]:
        #x1=0
        for x1 in [0,1,2,3,4,5]:
            if alien[y1][x1] == 0:
                fill(255)
                ellipse(x1*100+50,y1*50+50,30,30)
                #y1=y1+1
            elif alien[y1][x1] == 1:
                print("pew")
            #x1=x1+1
#Bullet
    global bullet
    if bullet == True:
        fill(0,255,80)
        noStroke
        rect(bulletX + 30,y,10,10)
    if y != 605:
        y = y - 7
        if y <= 0:
            y = 605
    if y == 605 and keyPressed and key == 'p': 
        bullet = True
        bulletX = x
        y = y - 1
    if y == y1 and x1:
        alien[y1][x1] == 1
#PLayer

    fill(0,255,80)
    noStroke
    rect(x,570, 70,40)
    if keyPressed and key == 'a':
        x=x-3
    if keyPressed and key == 'd':
        x=x+3
        

        
    
        