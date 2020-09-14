import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(100000)

n=int(input())
turtle.left(90)
for i in range(n):	
	for j in range(360):
		turtle.forward(i)
		turtle.right(1)
	for j in range(360):
		turtle.forward(i)
		turtle.left(1)
		


input()
