import turtle

class Paddle(turtle.Turtle):
    """
    The player-controlled paddle. Inherits from turtle.Turtle.
    Uses boolean flags for smooth, continuous movement per frame.
    """
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
        """Moves the paddle each frame, clamping X-coordinates so it doesn't leave the screen."""
        if self.is_moving_left:
            new_x = self.xcor() - 5  # Smaller step because it updates every frame now
            if new_x < -250:
                new_x = -250
            self.setx(new_x)
        if self.is_moving_right:
            new_x = self.xcor() + 3
            if new_x > 250:
                new_x = 250
            self.setx(new_x)
