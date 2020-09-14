import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(10000000)

def star(n,k,R):
	for i in range(n+1):
		turtle.goto(R*np.cos(np.pi*2*i*k/n),R*np.sin(np.pi*2*i*k/n))

n=int(input())
R=int(input())
if n%2==1 :
	k=(n-1)//2
	turtle.penup()
	turtle.goto(R,0)
	turtle.pendown()
	star(n,k,R)
else:
	k=(n-2)//2
	turtle.penup()
	turtle.goto(R,0)
	turtle.pendown()		
	star(n,k,R)
	turtle.penup()
	turtle.goto(-R,0)
	turtle.pendown()	
	star(n,k,-R)

input()
