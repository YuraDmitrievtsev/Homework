import turtle
import numpy as nm

turtle.shape('turtle')
turtle.speed(100000)

for i in range(100):
	for j in range(4):	
		turtle.forward(10*i+10)
		turtle.left(90)
	turtle.right(135)
	turtle.penup()
	turtle.forward(10/nm.sqrt(2))
	turtle.left(135)
	turtle.pendown()


input()
