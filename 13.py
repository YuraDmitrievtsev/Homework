import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10000000)

def krug(x,y,r):
	turtle.penup()
	turtle.goto(x+r,y)
	turtle.pendown()
	turtle.begin_fill()	
	for i in range(360):
		turtle.forward(r*2*np.pi/360)
		turtle.left(1)
	turtle.end_fill()

turtle.left(90)
turtle.color('yellow')
krug(0,0,50)
turtle.color('blue')
krug(20,20,10)
krug(-20,20,10)
turtle.color('black')
turtle.penup()
turtle.goto(0,10)
turtle.pendown()
turtle.goto(0,-10)
turtle.penup()
turtle.goto(20,-10)
turtle.pendown()
turtle.left(180)
for i in range(180):
	turtle.forward(20*2*np.pi/360)
	turtle.right(1)
turtle.penup()
turtle.goto(1000,1000)
input()
