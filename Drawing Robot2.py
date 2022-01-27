# Drawing Robot
# Reference from Udemy Python Bootcamp 2021

import turtle as t
import time as ti


def rect(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for i in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue') #background colour

# Making the Robot feet
t.goto(-100,-150)
rect(50,20,'blue')
t.goto(-30, -150)
rect(50,20,'blue')

# Making the Robot Leg
t.goto(-25,-50)
rect(15,100,'grey')
#t.goto(-55,-50)
#rect(15,100,'grey')
#rect(15,100,'Dodger blue')
#t.goto(-50,-50)
#rect(15,100,'grey')
#rect(15,100,'Dodger blue')
#t.goto(-60,-50)
#rect(15,100,'grey')
#rect(15,100,'Dodger blue')
t.goto(-65,-50)
rect(15,100,'grey')

# Making the Robot Body
t.goto(-90,100)
rect(100,150,'red')

# Making the Robot Left Arm
t.goto(-150,70)
rect(60,15,'grey')
t.goto(-150,110)
rect(15,40,'grey')

# Making the Robot Right Arm
t.goto(10,70)
rect(60,15,'grey')
#t.goto(55,1100)
t.goto(55,55)
rect(15,40,'grey')

# Making the Robot's left Hand
t.goto(-155,130)
rect(25,25,'green')
t.goto(-147,130)
rect(10,15,t.bgcolor())

# Making the Robot's Right Hand
t.goto(50,15)
rect(25,25,'green')
t.goto(58,5)
rect(10,15,t.bgcolor())

# Making the Robot's Neck
t.goto(-50,120)
rect(15,20,'grey')


# Making the Robot's Head
t.goto(-85,170)
rect(80,50,'red')

# Making the Robot's pupil
t.goto(-60,160)
rect(30,10,'white')

# Making the Robot's eyeballs
#t.goto(-55,155)
t.goto(-60,160)
rect(5,5,'black')
#t.goto(-40,155)
t.goto(-45,155)
rect(5,5,'green')
#rect(5,5,'black')

# Making the Robot's mouth
t.goto(-65,138)
t.right(5)
rect(40,5,'black')


t.goto(-155,155)
t.pensize(1)
t.pendown()
t.color('blue')
for i in range(1,10):
    t.color('red')
    t.circle(i+15)
    t.left(10)

ti.sleep(10)
t.hideturtle()



