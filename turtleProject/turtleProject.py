import turtle as j

def main () :
    #t.hideturtle()
    #t.speed(0)
    j.setup(width=800 , height=800)
    j.title("Turtle Project - turtleIntro")
    j.bgcolor("#1de047")
    line ()
    square ()
    circle ()
    triangle ()
    j.exitonclick ()

def line () :
    j.pencolor('green')
    moveT(50 , 0)
    j.left(180)
    j.forward(100)

def square () :
    j.pencolor('blue')
    moveT(100, 100)
    j.forward(200)
    j.left(90)
    j.forward(200)
    j.left(90)
    j.forward(200)
    j.left(90)
    j.forward(200)
    j.left(90)

def circle () :
    j.pencolor('purple')
    moveT(0,300)
    j.circle(300)

def triangle () :
    j.pencolor('brown')
    moveT(200,-125)
    j.forward(400)
    j.right(120)
    j.forward(400)
    j.right(120)
    j.forward(400)

def moveT (x , y) :
    j.penup ()
    j.setpos(x , y)
    j.pendown ()

main ()
