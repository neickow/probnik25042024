from turtle import *

tracer(0)
screensize(3000, 3000)
n = 50
left(90)
down()
for j in range(4):
    for i in range(3):
        forward(2 * n)
        right(270)
    forward(5 * n)

up()
color('red')
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * n, y * n)
        dot(3)
done()
