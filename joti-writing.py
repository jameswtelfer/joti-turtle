import jotihelpers
from jotihelpers import *

bringWindowToFront()

myTurtle = turtle

myTurtle.shape('turtle')
myTurtle.width('7')
myTurtle.pencolor('white')
myTurtle.bgcolor('purple')

pu()
setpos(-250,200)
pd()

myTurtle.fd(100)
myTurtle.bk(50)
myTurtle.rt(90)
myTurtle.fd(80)
myTurtle.rt(90)
myTurtle.fd(50)

myTurtle.pu()
myTurtle.rt(180)
myTurtle.fd(150)
myTurtle.pd()

myTurtle.circle(40, 360)

myTurtle.pu()
myTurtle.fd(100)
myTurtle.lt(90)
myTurtle.pd()

myTurtle.fd(80)
myTurtle.lt(90)
myTurtle.fd(50)
myTurtle.rt(180)
myTurtle.fd(100)

myTurtle.pu()
myTurtle.fd(20)
myTurtle.rt(90)
myTurtle.pd()

myTurtle.fd(80)

myTurtle.ht()

myTurtle.done()
