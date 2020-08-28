import turtle
from random import *

def generate():
    number = "0x"
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for i in range(0, 6):
        number = number + digits[randint(0, len(digits)-1)]
    return number


def make_darker(color):
    new_color = max(0, int(color, 0)-100)
    new_color = hex(new_color)
    return str(new_color)


def get_color_pair():
    hex_num = str(generate())
    dark_hex = make_darker(hex_num)
    hex_num = hex_num[2:].zfill(6)
    dark_hex = dark_hex[2:].zfill(6)

    hex_num = '#' + hex_num
    dark_hex = '#' + dark_hex

    return dark_hex, hex_num

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(5.10)
tim.color("green")
tim.pensize(5)


def up():
    tim.setheading(90)
    tim.forward(40)

def w():
    tim.setheading(90)
    tim.forward(40)

def down():
    tim.setheading(270)
    tim.forward(40)

def s():
    tim.setheading(270)
    tim.forward(40)

def left():
    tim.setheading(180)
    tim.forward(40)

def a():
    tim.setheading(180)
    tim.forward(40)

def right():
    tim.setheading(0)
    tim.forward(40)

def d():
    tim.setheading(0)
    tim.forward(40)

def clickleft(x, y):
    color_pair = get_color_pair()
    tim.color(color_pair[0], color_pair[1])

turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(up, "w")
turtle.onkey(down, "Down")
turtle.onkey(down, "s")
turtle.onkey(left, "Left")
turtle.onkey(left, "a")
turtle.onkey(right, "Right")
turtle.onkey(right, "d")
turtle.onscreenclick(clickleft, 1)
turtle.mainloop()