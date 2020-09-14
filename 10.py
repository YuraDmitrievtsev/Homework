import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(100000)

n=int(input())

for i in range(n):	
	turtle.left(90)
	for j in range(360):
		turtle.forward(1)
		turtle.right(1)
	turtle.right(90)
	turtle.left(360/n)
		


input()
