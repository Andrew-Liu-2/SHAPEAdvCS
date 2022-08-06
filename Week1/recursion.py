# rubtime stack

import turtle


def factorial(n):
    if n == (1):
        return 1
    return n * factorial(n-1)


print(factorial(5))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

# we have optimize this by using a dictionary


print(fibonacci(10))


t = turtle.Turtle()

t.penup()
t.setpos(-100, 0)
t.left(90)
t.pendown()
t.speed(1)


def koch(t, order, size):

    if order == 0:
        t.forward(size)
    else:
        koch(t, order - 1, size//3)
        t.left(60)
        koch(t, order - 1, size//3)
        t.right(120)
        koch(t, order - 1, size//3)
        t.left(60)
        koch(t, order - 1, size//3)

# koch(t,4,300)


def triangle(t, size):
    for i in range(3):
        t.forward(size)
        t.left(120)
# triangle(t,200)


def ngon(t, sides, size):
    for i in range(sides):
        t.forward(size)
        t.left(180 - (180*(sides-2)/sides))
# ngon(t,20,30)


# this starts small then goes bigger
def sierpinski(t, k, size):
    if k == 0:
        triangle(t, size)
    else:
        sierpinski(t, k-1, size/2)
        t.forward(size/2)
        sierpinski(t, k-1, size/2)
        t.backward(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        sierpinski(t, k-1, size/2)
        t.right(120)
        t.forward(size/2)
        t.left(120)


# sierpinski(t, 6, 400)

# this starts big then goes smaller




def fractalTree(t, k, size):
    if (k == 0):
        t.forward(size)
    else:
        fractalTree(t, k-1, size/3)
        t.left(30)
        fractalTree(t, k-1, size/3)
        t.right(180)
        t.forward(size/3)
        t.left(120)
        fractalTree(t, k-1, size/3)


# fractalTree(t, 2, 300)

wn = turtle.Screen()
wn.exitonclick()
turtle.bye()





# Towers of Hamoi