import turtle
import math
import data as dat


def get_point(t1, t2, a):
    dx = t2[0] - t1[0]
    dy = t2[1] - t1[1]
    return t1[0] + a * dx / math.sqrt(dx ** 2 + dy ** 2), t1[1] + a * dy / math.sqrt(dx ** 2 + dy ** 2)


def sierpinski_triangle(size, n, t1, t2, t3):
    if n == 0:
        return
    a = size / 2
    t13 = get_point(t1, t3, a)
    t12 = get_point(t1, t2, a)
    t23 = get_point(t2, t3, a)
    turtle.penup()
    turtle.hideturtle()
    turtle.home()
    turtle.showturtle()
    turtle.goto(t13)
    turtle.pendown()
    turtle.forward(a)
    for _ in range(0, 2):
        turtle.right(120)
        turtle.forward(a)
    sierpinski_triangle(a, n-1, t1, t12, t13)
    sierpinski_triangle(a, n-1, t13, t23, t3)
    sierpinski_triangle(a, n-1, t12, t2, t23)


if dat.SIZE <= 0:
    print('Error SIZE>0')
    exit()

if dat.N < 0:
    print('Error N>=0')
    exit()

turtle.penup()
turtle.setx(-150)
turtle.sety(-150)
turtle.pendown()

pos1 = turtle.pos()
turtle.forward(dat.SIZE)
pos2 = turtle.pos()
turtle.left(120)
turtle.forward(dat.SIZE)
pos3 = turtle.pos()
turtle.left(120)
turtle.forward(dat.SIZE)
sierpinski_triangle(dat.SIZE, dat.N, pos1, pos2, pos3)
turtle.exitonclick()
