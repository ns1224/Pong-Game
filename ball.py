from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, axis='y'):
        if axis == 'y':
            self.y_move *= -1
        else:
            self.x_move *= -1
            self.move_speed *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.move_speed = 0.1
        self.bounce('x')
