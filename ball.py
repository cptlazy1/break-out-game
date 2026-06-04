import turtle

class Ball(turtle.Turtle):
    """
    The moving ball. 
    dx and dy represent the change in X and Y coordinates per frame.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Movement speeds
        self.dx = 0.5
        self.dy = 0.5
        
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
