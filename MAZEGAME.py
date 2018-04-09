import turtle
 
 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)
 
 
 
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
 
levels = [""]
 
       
level_1 = [
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
            "X  XXXXXXX          XXXXX"
            "X  XXXXXXX  XXXXXX  XXXXX"
            "X       XX  XXXXXX  XXXXX"
            "X       XX  XXX        XX"
            "XXXXXX  XX  XXX        XX"
            "XXXXXX  XX  XXXXXX  XXXXX"
            "XXXXXX  XX    XXXX  XXXXX"
            "X  XXX        XXXX  XXXXX"
            "X  XXX  XXXXXXXXXXXXXXXXX"
            "X         XXXXXXXXXXXXXXX"
            "X                XXXXXXXX"
            "XXXXXXXXXXXX     XXXXX  X"
            "XXXXXXXXXXXXXXX  XXXXX  X"
            "XXX  XXXXXXXXXX         X"
            "XXX                     X"
            "XXX         XXXXXXXXXXXXX"
            "XXXXXXXXXX  XXXXXXXXXXXXX"
            "XXXXXXXXXX              X"
            "XX   XXXXX              X"
            "XX   XXXXXXXXXXXXX  XXXXX"
            "XX    XXXXXXXXXXXX  XXXXX"
            "XX           XXXX       X"
            "XXXX                    X"
            "XXXXXXXXXXXXXXXXXXXXXXXXX"
           ]
 
levels.append(level_1)
 
 
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
 
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
 
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
 
 
pen = Pen()
 
setup_maze(levels[1])
 
while True:
    pass
