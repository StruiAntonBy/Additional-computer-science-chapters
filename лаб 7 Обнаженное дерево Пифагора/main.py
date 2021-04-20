import turtle
import data as dat


def blown_pythagorean_tree(size, n, k, angel_a, angel_b):
    if n == 0:
        return
    turtle.forward(size)
    pos1 = turtle.pos()
    angel = turtle.heading()

    turtle.left(angel_a)
    blown_pythagorean_tree(size * k, n - 1, k, angel_a, angel_b)

    turtle.penup()
    turtle.hideturtle()
    turtle.home()
    turtle.showturtle()
    turtle.goto(pos1)
    turtle.left(angel)
    turtle.pendown()

    turtle.right(angel_b)
    blown_pythagorean_tree(size * k, n - 1, k, angel_a, angel_b)


turtle.penup()
turtle.sety(-200)
turtle.pendown()
turtle.left(90)

if dat.N < 0:
    print('Error N>=0')
    exit()

if dat.SIZE <= 0:
    print('Error SIZE>0')
    exit()

if dat.K >= 1 or dat.K <= 0:
    print('Error 0<K<1')
    exit()

if dat.ANGLE_A < 0 or dat.ANGLE_B < 0 or dat.ANGLE_A > 360 or dat.ANGLE_B > 360:
    print('Error 0<=α<=360 and 0<=β<=360')
    exit()


blown_pythagorean_tree(dat.SIZE, dat.N, dat.K, dat.ANGLE_A, dat.ANGLE_B)
turtle.exitonclick()
