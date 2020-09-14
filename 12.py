import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10000000)

turtle.left(90)
for i in range(100):
	for j in range(180):
		turtle.forward(2)
		turtle.right(1)
	for j in range(180):
		turtle.forward(1)
		turtle.right(1)
		


input()
