import turtle

import math
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Spave Invaders")
#sets the border to have a white line around it
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-250,-250)
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#sets score to zero
score = 0
#makes the score white and show up on the screne
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left",font=("Aridal", 14, "normal"))
score_pen.hideturtle()
#sets the player to zero
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
#sets the characters speed
playerspeed = 15

#sets number of enemies
number_of_enemies = 10

enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
#shape of enemies and where they start
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(-100,250)
    enemy.setposition(x, y)
#speed of enemy
enemyspeed = 2
#bullet shape
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)

bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
#bullet speed
bulletspeed = 20

#define bullet state
#ready - ready to fire

bulleststate = "ready"
#moves player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
#moves player right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
#has the bullet fire
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

#true or false for when bullet his enemy
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) +math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
#sets enemies speed
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1


        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
#collision with enemy
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200,200)
            y = random.randint(-100,250)
            enemy.setposition(x, y)

            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left",font=("Aridal", 14, "normal"))
#collision with player
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #if bulletstate == "fire":
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
#bullet y positions
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"




#closes project
delay = raw_input("Press enter to finish")
wn.exitonclick()
