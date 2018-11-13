import turtle

black_color = (0.0, 0.0, 0.0)
white_color = (1.0, 1.0, 1.0)
red_color = (1.0, 0.0, 0.0)
green_color = (0.0, 1.0, 0.0)
blue_color= (0.0, 0.0, 1.0)
hex_color = "#ffe063"

pen = turtle.Pen()

def main():
    turtle.bgcolor('red')
    mystery_drawing_one(90)
    pen.penup()
    pen.setpos(0,100)
    pen.pendown()
    mystery_drawing_two(90)
    pen.penup()
    pen.setpos(100,50)
    pen.pendown()
    mystery_drawing_three(90)
    pen.penup()
    pen.setpos(220,50)
    pen.pendown()
    mystery_drawing_four(90)
    turtle.exitonclick()

def mystery_drawing_one(angle):
    for x in range(0,4):
        pen.forward(50)
        pen.left(angle)

def mystery_drawing_two(angle):
    turtle.pencolor('green')
    for x in range(0,4):
        pen.forward(50)
        pen.left(angle)

def mystery_drawing_three(angle):
    turtle.pencolor('white')
    for x in range(0,2):
        pen.forward(100)
        pen.left(angle)
        pen.forward(50)
        pen.left(angle)

def mystery_drawing_four(angle):
    turtle.pencolor('blue')
    for x in range(0,2):
        pen.forward(100)
        pen.left(angle)
        pen.forward(50)
        pen.left(angle)


main()
