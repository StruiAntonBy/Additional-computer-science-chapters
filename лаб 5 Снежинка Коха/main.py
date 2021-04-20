import turtle
import data as dat


def koch_line(arrow, size, n):
    if n == 0:
        arrow.forward(size)
    else:
        koch_line(arrow, size/3, n-1)
        arrow.left(60)
        koch_line(arrow, size / 3, n - 1)
        arrow.right(120)
        koch_line(arrow, size / 3, n - 1)
        arrow.left(60)
        koch_line(arrow, size / 3, n - 1)


def koch_snowflake(arrow, size, n):
    arrow.left(60)
    koch_line(arrow, size, n)
    for _ in range(0, 2):
        arrow.right(120)
        koch_line(arrow, size, n)


if dat.N < 0:
    print("Error N>=0")
    exit()
turtle.penup()
turtle.setx(-150)
turtle.pendown()
koch_snowflake(turtle, dat.SIZE, dat.N)
turtle.exitonclick()
