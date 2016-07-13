from Myro import *
init("sim")
#loops



#Functions
def drawK(size):
    turnBy(90,"deg")
    forward(2,size)
    backward(1,size)
    turnBy(-35,"deg")
    forward(1,size)
    backward(1,size)
    turnBy(-95,"deg")
    forward(1,size+.2)
    turnBy(30,"deg")
    
def drawB(size):
    turnBy(90,"deg")
    forward(2,1)
    motors(size*5,0,.5)
    turnBy(270,"deg")
    motors(size*5,0,.5)




#Code- actual work being done
penDown()
drawK(1)
penUp()
penDown()
drawB(8)
