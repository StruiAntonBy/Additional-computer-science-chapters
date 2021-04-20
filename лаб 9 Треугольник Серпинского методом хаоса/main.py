import turtle
import data as dat
from random import randint


def sierpinski_triangle(point_a, point_b, point_c, current_point, num_iter):
    for _ in range(0, num_iter):
        i = randint(0, 2)
        if i == 0:
            p = point_a
        elif i == 1:
            p = point_b
        else:
            p = point_c
        current_point = ((p[0] + current_point[0]) / 2, (p[1] + current_point[1]) / 2)
        turtle.penup()
        turtle.goto(current_point)
        turtle.pendown()
        turtle.circle(1)


if dat.SIZE <= 0:
    print('Error SIZE>0')
    exit()

if dat.NUM_ITER <= 0:
    print('Error NUM_ITER>0')
    exit()

if dat.SPEED < 0 or dat.SPEED > 10:
    print('Error 0<=SPEED<=10')
    exit()

turtle.penup()
turtle.setx(-dat.SIZE / 2)
turtle.sety(-dat.SIZE / 2)
start_pos = turtle.pos()
turtle.pendown()

turtle.speed(dat.SPEED)
a, b, c = start_pos, (start_pos[0] + dat.SIZE, start_pos[1]), (start_pos[0] + dat.SIZE / 2, start_pos[1] + dat.SIZE)
random_point = (start_pos[0] + randint(-dat.SIZE, dat.SIZE) * 1.1, start_pos[1] + randint(-dat.SIZE, dat.SIZE) * 1.1)
for point in [a, b, c, random_point]:
    turtle.penup()
    turtle.goto(point)
    turtle.pendown()
    turtle.circle(1)
sierpinski_triangle(a, b, c, random_point, dat.NUM_ITER)
turtle.exitonclick()
