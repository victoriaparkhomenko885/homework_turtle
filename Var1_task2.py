# logarithmic spiral
import turtle
import math

FIXED = 1.3

counter = 1

spiral = turtle.Turtle()
spiral.speed(10)

for i in range(12):
    for j in range(40):    
        spiral.right(math.log(300/3.14))
        spiral.forward(counter)
    counter *= FIXED

input()
