import turtle
import math
import random
import os
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)
wn.tracer(0)

#add images


#create pen
class Pen(turtle.Turtle):
    
    
    def __init__(self):
        
        turtle.Turtle.__init__(self)
        
        
        
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    
    def __init__(self):
        
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0


    def up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y) 
        
        
        
    def down(self):
        
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            
            self.goto(move_to_x, move_to_y)
        
        
    def left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        
        
    def right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        

        
    
        
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)







        

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle    

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])


    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

                       
#create level list
levels = [""]
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XX  XXXXXXX          EXX",
"X           XXXXXX  XXXX",
"X  XXXXXXX          XXXX",
"X  XXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXX",
"X                      X",
"XXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXX",
"XXXXXX                TX",
"XXXXXX   XXXXXXXXXXXXX X",
"XXXXXX   XXXXXXXXXXXXX X",
"X                      X",
"XXXXE    XXXXXXXXXX    X",
"X        XXXXXXXXXXX XXX",
"XXXXXX   XXXXXXXXXXX XXX",
"X                      X",
"XXXXXX   XXXX   XXXXXXXX",
"XXXXXX   XXXX   XXXXXXXX",
"XXXXX    EXXX          X",
"X               X      X",
"XXXXXXX   XXXXXXX  XXXXX",
"XXXXXX    XXXXXXX  XXXXX",
"XXXXXXXX           XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXX"
]

#TREASURE!!!
treasures = []
levels.append (level_1)

enemies = []

def setup_maze(level):
    
    for y in range(len(level)):
        for x in range(len(level[y])):
            
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                
                
                pen.goto(screen_x, screen_y)
                pen.stamp()
                #add cord to wall
                walls.append((screen_x, screen_y))

        
            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
                                                   
            if character == "E":
                enemies.append(Treasure(screen_x, screen_y))    
#create walls                
walls = []
                
               



#class instances
pen = Pen()
player = Player()

setup_maze(levels[1])


#keyboard binding
turtle.listen()
turtle.onkey(player.left,"a")
turtle.onkey(player.right,"d")
turtle.onkey(player.up,"w")
turtle.onkey(player.down,"s")
wn.tracer(0)

for enemy in enemies:
    
    
    turtle.ontimer(enemy.move, t=250)



#main game loop
while True:
    for treasure in treasures:
        
        if player.is_collision(treasure):
            player.gold += treasure.gold
            
            print ("Player's Gold {}".format(player.gold))
            
            treasure.destroy()
            treasures.remove(treasure)

    for enemy in enemies:
        
        
         
        if player.is_collision(enemy):
            
            print ("You Lose!")
        
    wn.update()
