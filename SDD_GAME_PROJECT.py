import sys

def gameStart(): 
    UserName = input('Hello young traveller may I ask what is your name: ')
    print('So your name is ' + UserName + '? What a wonderful name for our next Lengendary Warrior!')

    
def WarriorQuestion():
    validInput = False
    while validInput == True:
        Join = input('You want to become a warrior right? Yes or No: ') .lower()
        if Join.startswith('y'):
           print("Great, welcome to the game called Eindhoven " + UserName + '!')
           validInput = False
        elif Join.startswith('n'):
              print ("Sorry for asking, comeback when you are ready.")
              sys.exit()
        else:
              print ("Sorry, that was an invalid command!")
              validInput = False
        

def introduction():
    print("This land was once a joyful, charming place which was populated by the Elves. but one day the Giants decided to takeover the Elves country. War immediatley broke loose amd the Elves were enslaved. Until this day they are still being held captive and are waiting for a Lengendary Warrior to break them out.") 
def Chooseclass():
    print('Please select your class.')
    UserClass = input('You have the choice of Fighter, Marksmen, or Tank: ')

gameStart()
WarriorQuestion()
introduction()
Chooseclass()
