Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
s = turtle.pen()
t = turtle.Turtle()
def half_inside_circle():
    for i in range(12):
        t.circle(64.3, 180)
        t.rt(150)

        
def line_half_circle():
    n = 255
    while n >= -45:
        t.pendown()
        t.home()
        t.lt(n)
        t.fd(248.44)
        t.penup()
        t.penup()
        t.home()
        n = n - 30

        
t.penup()
t.goto(-64.3,-240)
t.rt(90)
t.pendown()
half_inside_circle()
t.penup()
t.lt(90)
t.fd(128.6)
line_half_circle()
def mid_flower():
    for i in range(100):
        t.speed(50)
        t.circle(80)
        t.rt(3.6)

        
t.penup()
mid_flower()
t.pendown()
mid_flower()
