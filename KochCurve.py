"""Created on 21 Jan 2019

Coding Exercise: Write a turtle program to draw Koch Curve

Solutions @author: SjGanguly (trying_ai)
"""
def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        t.fd(n)
        return
    m = n/3.0
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

import turtle

bob = turtle.Turtle()
x =600
koch (bob,x)
turtle.exitonclick()
