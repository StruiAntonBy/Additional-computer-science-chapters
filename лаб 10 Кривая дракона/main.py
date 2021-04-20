import turtle
import sys
import config
import data as dat
import os


def print_path_dragon_line(n, var, file=sys.stdout):
    if n == 0:
        pass
    else:
        print_path_dragon_line(n - 1, 'R', file=file)
        print(var, end='', file=file)
        print_path_dragon_line(n - 1, 'L', file=file)


def draw_dragon_line(size, path):
    for x in path:
        if x == 'R':
            turtle.right(90)
            turtle.forward(size)
        elif x == 'L':
            turtle.left(90)
            turtle.forward(size)
        else:
            raise ValueError


if dat.SIZE <= 0:
    print('Error SIZE>0')
    exit()

if dat.N < 0:
    print('Error N>=0')
    exit()

turtle.left(90)
turtle.forward(dat.SIZE)

with open(config.FILE_NAME, 'w') as f:
    print_path_dragon_line(dat.N, 'R', file=f)

with open(config.FILE_NAME, 'r') as f:
    res = f.read()

if os.path.isfile(config.FILE_NAME):
    os.remove(config.FILE_NAME)

draw_dragon_line(dat.SIZE, res)
turtle.exitonclick()
