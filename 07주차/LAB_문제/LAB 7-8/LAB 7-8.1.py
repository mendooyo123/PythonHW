#LAB 7-8 /문제_1 멘두요
import turtle as t 
t.color('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.setheading(90)
t.color('red')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.setheading(180)
t.color('yellow')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.setheading(270)
t.color('green')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.done()