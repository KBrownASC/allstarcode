from Myro import *
init("sim")

#variables
size=2
time=0
bigTime=2
turnRight = 90

#loopvariables
loopSquare=0

#code
penDown()
while time<2.1:
    time=time+.5
    wait(.1)
    while loopSquare<4:
        forward(size,time)
        turnBy(turnRight,"deg")
        loopSquare=loopSquare+1
    loopSquare=0