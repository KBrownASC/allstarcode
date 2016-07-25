from random import*
from time import*


x = -5
y = 0
score = 0
lose = 0
SpeedX = 2
SpeedUp = 0


Alphabet = ["a", "b", "c", "d",
            "e", "f", "g", "h",
            "i", "j", "k", "l",
            "m", "n", "o", "p",
            "q", "r", "s", "t",
            "u", "v", "w", "x",
            "y", "z"]
Alphabet2 = ["a", "b", "c", "d",
            "e", "f", "g", "h",
            "i", "j", "k", "l",
            "m", "n", "o", "p",
            "q", "r", "s", "t",
            "u", "v", "w", "x",
            "y", "z"]


def setup():
    global score
    background(0,80,255)
    if score >= 30:
        background(255,0,0)
    if score >= 60:
        background(255,0,255)
    size(800,400)
        

    
    
    
    
    
rLet= Alphabet[randrange(25)]
y = randrange(20,380)
rLet2= Alphabet2[randrange(25)]  
 
def draw():
    
    global x
    global y
    global rLet
    global score
    global lose
    global SpeedX
    global SpeedUp
    global rLet2

#First Letter
    if x > 800:
        rLet = Alphabet[randrange(25)]
        x=0
        y = randrange(20,380)
        lose = lose + 1
    if keyPressed and key == rLet:
        rLet= Alphabet[randrange(25)]
        x=0
        SpeedUp= SpeedUp + 1
        if SpeedUp == 5:
            SpeedX=SpeedX+.5
            SpeedUp = 0
        score=score+1
        y= randrange(20,380)
    if score == 30:
        background(255,0,0)

        
    background(0,80,255)
    if score >= 30:
        background(255,0,0)
    if score >= 60:
        background(255,0,255)
    textSize(32)
    text(rLet,x,y)
    x = x + SpeedX


    textSize(10)
    text("score",10,20)
    
    textSize(10)
    text(score,40,20)
    
    
    textSize(10)
    text("missed", 700,20)
    
    textSize(10)
    text(lose,750,20)

    textSize(10)
    text("/5",770,20)
    
    if lose == 5:
        background(1)
        textSize(40)
        text("YOU LOSE",300,200)
        SpeedX = SpeedX - 1
        
    if lose >= 7:
        background(1)
        textSize(40)
        text("YOU LOST!!!!!!!!",250,200)
        text("click to restart",250,250)
    if mousePressed and lose >= 7:
        background(220,220,0)
        score = 0
        lose = 0
        SpeedX = 2
        x=0 