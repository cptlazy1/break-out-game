import turtle
import random
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

# Score and Lives System
score = 0
lives = 3
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))

# Game Over elements
button_pen = turtle.Turtle()
button_pen.color("white")
button_pen.penup()
button_pen.hideturtle()

bricks = []
color_list = ["red", "blue", "green", "yellow", "orange"]
def create_bricks():
    for brick in bricks:
        brick.goto(1000, 1000)
    bricks.clear()
    for y in range(250, 100, -30):
        for x in range(-250, 260, 70):
            new_brick = Brick(x, y, random.choice(color_list))
            bricks.append(new_brick)

create_bricks()
game_state = "playing"

def handle_click(x, y):
    """
    Fired automatically when the screen is clicked.
    Checks if the (x, y) click coordinates fall inside our invisible UI button bounding boxes.
    """
    global game_state, score, lives
    if game_state == "game_over":
        if (-100 < x < 100) and (-65 < y < -25):
            # Restart the game!
            score = 0
            lives = 3
            pen.clear()
            pen.goto(0, 360)
            pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))
            button_pen.clear()
            
            player_paddle.goto(0, -350)
            game_ball.goto(0, 0)
            game_ball.dx = 1.5
            game_ball.dy = -1.5
            
            create_bricks()
            game_state = "playing"
        elif (-100 < x < 100) and (-105 < y < -65):
            wn.bye()  # Close the game window


wn.onscreenclick(handle_click)

# Main game loop
while True:
    wn.update()
    
    if game_state == "playing":
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
            lives -= 1
            pen.clear()
            pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))
            game_ball.goto(0, 0)
            game_ball.dy *= -1
            
            if lives == 0:
                game_state = "game_over"
                game_ball.goto(1000, 1000)
                player_paddle.goto(1000, 1000)
                for b in bricks:
                    b.goto(1000, 1000)
                bricks.clear()
                
                pen.goto(0, 0)
                pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
                
                button_pen.goto(0, -60)
                button_pen.write("[ PLAY AGAIN ]", align="center", font=("Courier", 24, "normal"))

                button_pen.goto(0, -100)
                button_pen.write(" [ QUIT ] ", align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions
        # We check both Y-height (is it touching the paddle) and X-width (is it within the 100px width)
        if (-340 > game_ball.ycor() > -350) and (
                player_paddle.xcor() + 50 > game_ball.xcor() > player_paddle.xcor() - 50):
            game_ball.sety(-340)
            game_ball.dy *= -1

        # Brick collisions
        for brick in bricks:
            if game_ball.distance(brick) < 35:
                brick.goto(1000, 1000)
                bricks.remove(brick)
                score += 10
                pen.clear()
                pen.goto(0, 360)
                pen.write(f"Score: {score}  Lives: {lives}", align="center", font=("Courier", 24, "normal"))
                game_ball.dy *= -1
                break
