from random import *
from time import *
from sys import *


ColorMode=0
sz=3
#Canvas
def setup():
    background(255,255,255)
    size(500,500)
    
#colorssss
#red
    fill(255,0,0)
    rect(0,0,25,50)
#green
    fill(0,255,0)
    rect(0,50,25,50)
#yellow
    fill(180,180,0)
    rect(0,100,25,50)
#blue
    fill(0,0,255)
    rect(0,150,25,50)
#black
    fill(0,0,0)
    rect(0,200,25,50)   










#Drawing tool
def draw():
    global ColorMode
    global sz
    

    #DRAW FUNCTION
    if mouseX<26 and mouseY<50 and mousePressed and (mouseButton == LEFT):
        ColorMode=1
    elif mouseX<26 and mouseY<100 and mousePressed and (mouseButton == LEFT):
        ColorMode=2
    elif mouseX<26 and mouseY<150 and mousePressed and (mouseButton == LEFT):
        ColorMode=3
    elif mouseX<26 and mouseY<200 and mousePressed and (mouseButton == LEFT):
        ColorMode=4
    elif mouseX<26 and mouseY<250 and mousePressed and (mouseButton == LEFT):
        ColorMode=5
#RED        
    if mousePressed and (mouseButton == LEFT) and ColorMode==1:
        fill(255,0,0)
        stroke(255,0,0)
        ellipse(mouseX,mouseY,sz,sz)
#Green
    if mousePressed and (mouseButton == LEFT) and ColorMode==2:
        fill(0,255,0)
        stroke(0,255,0)
        ellipse(mouseX,mouseY,sz,sz)
#Yellow
    if mousePressed and (mouseButton == LEFT) and ColorMode==3:
        fill(180,180,0)
        stroke(180,180,0)
        ellipse(mouseX,mouseY,sz,sz)
#Blue
    if mousePressed and (mouseButton == LEFT) and ColorMode==4:
        fill(0,0,255)
        stroke(0,0,255)
        ellipse(mouseX,mouseY,sz,sz) 
#Black
    if mousePressed and (mouseButton == LEFT) and ColorMode==5:
        fill(0,0,0)
        stroke(0,0,0)
        ellipse(mouseX,mouseY,sz,sz)    
#ERASE FUNCTION
    if mousePressed and (mouseButton == RIGHT):
        fill(255)
        stroke(255)
        ellipse(mouseX,mouseY,50,50) 
#Complete ErASE FUnCTION 
    if keyPressed and key == 'e' or key == 'E':
        fill(255,255,255)
        stroke(255,255,255)
        rect(25,0,474,500)       
    if keyPressed and key ==']':
        sz=sz+1
    if keyPressed and key =='[':
        sz=sz-1



#ColorsSelect

#Colors



#Resz





#BrushType




#Tools





#Save Option 