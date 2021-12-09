from turtle import Turtle


class Court(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.color("white")
        self.draw()
        self.pendown()
        self.outlines()

    def draw(self):
        self.penup()
        self.goto(-400, 300)
        self.pendown()
        self.begin_fill()
        coordinates = [(400, 300), (400, -300), (-400, -300), (-400, 300)]
        for x, y in coordinates:
            self.goto(x, y)
        self.end_fill()

    def outlines(self):
        self.penup()
        self.color("black")
        self.goto(0, 300)
        self.pendown()
        self.goto(0, -300)
        self.penup()
        self.goto(0, -50)
        self.pendown()
        self.circle(50)



