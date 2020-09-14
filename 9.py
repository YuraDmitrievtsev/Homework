import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10000000)

for n in range(1,100):
	turtle.penup()
	turtle.goto(10*n,0)
	turtle.pendown()
	for i in range(n+1):
		turtle.goto(10*n*np.cos(np.pi*2*i/n),10*n*np.sin(np.pi*2*i/n))
		


input()
