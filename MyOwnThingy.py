from Myro import *
from Graphics import *
from random import *

#Browser
#width=500
#length=500
#sim = Simulation("My Own Application", width, length, Color("pink"))


def makeButton(sizes):
    shape = RoundedRectangle((sizes, sizes), (200-sizes, 200-sizes), sizes)
    shape.fill = Color("green")#outlayer of button color
    shape.draw(win)
    shape = RoundedRectangle((sizes+10, sizes+10), (190-sizes, 190-sizes), sizes)
    shape.fill = Color("lightgreen")#innerlayer of button color
    shape.draw(win)


win = Window("myStuff", 200, 200)
while getMouse():
    makeButton(45)
    
    stop()
