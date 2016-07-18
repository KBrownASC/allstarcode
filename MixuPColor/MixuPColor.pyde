from random import *
from time import *


r = 180
g = 180
b = 0
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
    fill(r,g,b)
    stroke(r,g,b)
    ellipse(mouseX,mouseY,40,40)
    rotate(90,20,20,20)
    ellipse(mouseX-45,mouseY-45,20,20)
    ellipse(mouseX-45,mouseY+45,20,20)
    ellipse(mouseX+45,mouseY+45,20,20)
    ellipse(mouseX+45,mouseY-45,20,20)
    r=r+N
    g=g+D
    b=b+J
    if r == 255:
        N=-1
    if r == 0:
        N=1
    if g==255:
        D=-1
    if g==0:
        D=1
    if b==255:
        J=-1
    if b==0:
        J=1

def mouseClicked():
    while True:
        sleep(2)