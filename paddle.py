import turtle

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -350)
        # Add movement state booleans
        self.is_moving_left = False
        self.is_moving_right = False

    def start_left(self):
        self.is_moving_left = True
        
    def stop_left(self):
        self.is_moving_left = False
        
    def start_right(self):
        self.is_moving_right = True
        
    def stop_right(self):
        self.is_moving_right = False

    def move(self):
        if self.is_moving_left:
            new_x = self.xcor() - 5  # Smaller step because it updates every frame now
            if new_x < -250:
                new_x = -250
            self.setx(new_x)
        if self.is_moving_right:
            new_x = self.xcor() + 5
            if new_x > 250:
                new_x = 250
            self.setx(new_x)
