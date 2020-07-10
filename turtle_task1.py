import turtle

brain = turtle.Turtle()

brain.screen.bgcolor("coral")
brain.speed(6)
brain.pensize(2)

def paint(space, color):
   brain.fillcolor(color)
   brain.begin_fill()
   
   for i in range(4):
       brain.forward(space)
       brain.left(90)

   brain.end_fill()

colors = ['yellow', 'red', 'lime', 'red']
for iter in range(4):
    paint(100,colors[iter])
    brain.left(90)

brain.up()
brain.color("blue")
brain.forward(200)
brain.down()
brain.left(90)
brain.circle(200)

input()
