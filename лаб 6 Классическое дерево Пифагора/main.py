import turtle
import math
import data as dat


def move_rotate(place, angel):
    turtle.penup()
    turtle.hideturtle()
    turtle.home()
    turtle.left(angel)
    turtle.showturtle()
    turtle.goto(place)
    turtle.pendown()


def paint_square(size, flag):
    angel, place1, place2 = None, None, None
    turtle.forward(size)

    if flag == 'right':
        angel = turtle.heading()
        place1 = turtle.pos()

    turtle.left(90)
    turtle.forward(size)

    if flag == 'right':
        place2 = turtle.pos()

    if flag == 'left':
        angel = turtle.heading()
        place1 = turtle.pos()

    turtle.left(90)
    turtle.forward(size)

    if flag == 'left':
        place2 = turtle.pos()

    turtle.left(90)
    turtle.forward(size)

    return angel, place1, place2


def pythagorean_tree(size, angel_a, angel_b, place1, place2, angel_s, n):
    if n == 0:
        return

    size1 = math.cos(math.radians(angel_a)) * size
    size2 = math.cos(math.radians(angel_b)) * size

    move_rotate(place2, angel_s)
    turtle.right(90 - angel_a)
    angel, place3, place4 = paint_square(size1, 'left')
    pythagorean_tree(size1, angel_a, angel_b, place3, place4, angel, n - 1)

    move_rotate(place1, angel_s)
    turtle.right(angel_b)
    angel, place3, place4 = paint_square(size2, 'right')
    pythagorean_tree(size2, angel_a, angel_b, place3, place4, angel, n - 1)


if dat.SIZE <= 0:
    print('Error SIZE>0')
    exit()

if dat.N < 0:
    print('Error N>=0')
    exit()

if dat.SPEED < 0 or dat.SPEED > 10:
    print('Error 0<=SPEED<=10')
    exit()

if dat.ANGLE_A <= 0 or dat.ANGLE_B <= 0:
    print('Error (ANGLE_A or ANGLE_B)>0')
    exit()

if dat.ANGLE_A + dat.ANGLE_B != 90:
    print('Error ANGLE_A+ANGLE_B==90')
    exit()

turtle.speed(dat.SPEED)
turtle.penup()
turtle.sety(-200)
turtle.setx(-dat.SIZE / 2)
turtle.pendown()
start_angle, pos1, pos2 = paint_square(dat.SIZE, 'left')
pythagorean_tree(dat.SIZE, dat.ANGLE_A, dat.ANGLE_B, pos1, pos2, start_angle, dat.N)
turtle.exitonclick()
