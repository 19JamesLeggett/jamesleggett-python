import turtle as j

def main () :
    j.setup(width=800 , height=800)
    j.title("Turtle Project - turtleIntro")
    j.bgcolor("#1de047")
    #j.hideturtle()
    j.speed(0)
    circle ()
    square ()
    triangle ()
    rectangle ()
    j.exitonclick ()

def square () :
    j.pencolor('blue')
    moveT(100, 100)
    j.forward(50)
    j.left(90)
    j.forward(50)
    j.left(90)
    j.forward(50)
    j.left(90)
    j.forward(50)
    j.left(90)

def circle () :
    j.pencolor('orange')
    moveT(-100,-300)
    j.circle(50)

def triangle () :
    j.pencolor('brown')
    moveT(200,-125)
    j.forward(100)
    j.right(120)
    j.forward(100)
    j.right(120)
    j.forward(100)

def rectangle () :
    j.pencolor('purple')
    moveT(-300, 150)
    j.forward(100)
    j.right(90)
    j.forward(150)
    j.right(90)
    j.forward(100)
    j.right(90)
    j.forward(150)

def moveT (x , y) :
    j.penup ()
    j.setpos(x , y)
    j.pendown ()

main()
