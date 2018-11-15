import turtle as j

def main () :
    j.setup(width=800 , height=800)
    j.title("Turtle Project - turtleIntro")
    j.bgcolor("#1de047")
    j.hideturtle()
    j.speed(0)
    inputinfo ()
    #circle ()
    j.exitonclick ()

def inputinfo () :
    c = input ('Input a color to draw with - ')
    l = int(input('Input the length in pixels of each side - '))
    n = int(input('Input the number of sides for your polygon - '))
    if n<=2 :
        error()
    something (c , l , n)


def something (c , l , n) :
    j.pencolor(c)
    j.penup()
    b = (l / -2)
    c = (l / 2)
    j.setpos(b , c)
    j.pendown ()
    a = 360 / n
    for x in range(0,n) :
        j.forward(l)
        j. right(a)

def circle () :
    j.penup()
    j.setpos(-300,-300)
    j.pendown()
    j.circle(50)

def error () :
    p = input('You cant have polygon with 2 or less sides')

main ()
