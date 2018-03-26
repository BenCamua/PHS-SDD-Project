import sys

def WarriorQuestion():
    validInput = False
    while validInput == False:
        Join = input('You want to become a warrior right? Yes or No: ') .lower()
        if Join.startswith('y'):
           print("Great, welcome to the game called Eindhoven " + UserName + '!')
           validInput = True
           gameLoop()
        elif Join.startswith('n'):
              print ("Sorry for asking, comeback when you are ready.")
              sys.exit()
        else:
              print ("Sorry, that was an invalid command!")
              validInput = False
        

def gameLoop():
    print('yrdgfdg')
    

UserName = input('Hello young traveller may I ask what is your name: ')
print('So your name is ' + UserName + '? What a wonderful name for our next lengendary warrior!')

WarriorQuestion()
