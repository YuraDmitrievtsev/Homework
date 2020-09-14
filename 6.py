import turtle
import numpy as nm

turtle.shape('turtle')
turtle.speed(100000)

n=input()

for i in range(int(n)):
	turtle.forward(10000)
	turtle.backward(10000)
	turtle.left(360/int(n))


input()
