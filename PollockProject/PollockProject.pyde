from random import *
from time import *


r = range(255)
g = range(255)
b = range(255)
N= 1
D=1
J=1
value = 0
redRange= 1


def setup():
    size(500,500)
    background(255,255,255)

def draw():
    global r
    global g
    global b
    global N
    global D
    global J
    fill(choice(r),choice(g),choice(b))
    stroke(choice(r),choice(g),choice(b))
    ellipse(mouseX,mouseY,40,40)
    rotate(90,20,20,20)
    ellipse(mouseX-45,mouseY-45,20,20)
    ellipse(mouseX-45,mouseY+45,20,20)
    ellipse(mouseX+45,mouseY+45,20,20)
    ellipse(mouseX+45,mouseY-45,20,20)

def mouseClicked():
    while True:
        sleep(2)