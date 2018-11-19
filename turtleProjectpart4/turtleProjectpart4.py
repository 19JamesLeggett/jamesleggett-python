import turtle as j
import random
pen = j.Pen()

def main():
    j.setup(width=800 , height=800)
    j.title("Turtle Project - turtleIntro")
    j.bgcolor("black")
    #j.hideturtle()
    pen.speed(0)
    rosette2()
    rosette()
    pen.clear()
    circle()
    for x in range(0,4):
        pen.up()
        pen.goto(0,0)
        pen.down()
        square()
        pen.right(90)
    #triangle ()
    #rectangle ()
    j.exitonclick ()

def rosette():
    for x in range(0,50):
        pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
        pen.circle(100)
        pen.right(10)
def rosette2():
    for x in range(0,50):
        pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
        pen.circle(140)
        pen.right(10)

def circle():
    for x in range(0,500,10):
        pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
        pen.circle(x)
        pen.up()
        pen.right(90)
        pen.forward(10)
        pen.left(90)
        pen.down()

def square ():
    for x in range (0,500,10):
        pen.pencolor(random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100)
        pen.forward(x)
        pen.left(90)
        pen.forward(x)
        pen.left(90)
        pen.forward(x)
        pen.left(90)
        pen.forward(x)
        pen.left(90)



main()
