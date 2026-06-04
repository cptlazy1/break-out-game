import turtle
from paddle import Paddle
from ball import Ball
from brick import Brick

# Screen setup
wn = turtle.Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0) # Turns off automatic screen updates

# Create objects
player_paddle = Paddle()
game_ball = Ball()

# Keyboard bindings
wn.listen()
wn.onkeypress(player_paddle.start_left, "Left")
wn.onkeyrelease(player_paddle.stop_left, "Left")
wn.onkeypress(player_paddle.start_right, "Right")
wn.onkeyrelease(player_paddle.stop_right, "Right")

# Score System
score = 0
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Create Bricks
bricks = []
for y in range(250, 100, -30):
    for x in range(-250, 260, 70):
        new_brick = Brick(x, y)
        bricks.append(new_brick)

# Main game loop
while True:
    wn.update()
    game_ball.move()
    player_paddle.move()

    # Border checking
    if game_ball.xcor() > 290:
        game_ball.setx(290)
        game_ball.dx *= -1
        
    if game_ball.xcor() < -290:
        game_ball.setx(-290)
        game_ball.dx *= -1
        
    if game_ball.ycor() > 390:
        game_ball.sety(390)
        game_ball.dy *= -1
        
    if game_ball.ycor() < -390:
        game_ball.goto(0, 0)
        game_ball.dy *= -1 # reverse direction to start fresh

    # Paddle and ball collisions
    if (game_ball.ycor() < -340 and game_ball.ycor() > -350) and (game_ball.xcor() < player_paddle.xcor() + 50 and game_ball.xcor() > player_paddle.xcor() - 50):
        game_ball.sety(-340)
        game_ball.dy *= -1

    # Brick collisions
    for brick in bricks:
        if game_ball.distance(brick) < 35:
            brick.goto(1000, 1000) # Move off screen
            bricks.remove(brick)
            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
            game_ball.dy *= -1
            break # Only hit one brick per frame
