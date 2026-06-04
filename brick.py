import turtle


class Brick(turtle.Turtle):
    """
    A single target block. We move these off-screen when "destroyed" 
    because completely deleting objects in Turtle is complex.
    """
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3) # 60px wide, 20px tall
        self.penup()
        self.goto(x, y)
