from random import randint
import time
word = "a"
shield = 5
#The main function
def main():
    #This will trigger the introduction
    intro()
    while True:
        shield, word, finished = TakeTurn(word,shield)
        if finished:
            break
        if shield == 1:
            word1 = "shield"
        else:
            word1 = "shields"
        print ("You have",shield,word1)
    if shield < 1:
        print ("Sorry! You ran out of shields! You lose!")
    else:
        print ("You win")

#This function is the introduction to the program
def intro():
    time = [1,2.5, 2, 1.5, 1, 2, 1]
    text = ["You are lost in a maze, it is dark and you are lost",
         "Im afraid there are monsters here...", "BOO!",
         "You have five shields to protect you...","Use them well!",
         "Okay, let's go!"]
    print_on_a_timer(time, text)

#This function is the actual 'game' and will deterine what happens to the character    
def TakeTurn(word1,shield1):
    time.sleep(1.5)
    #This means that when the user reaches 0 shields, they lose.
    if shield1 < 1:
        return True
    #Whatever the user inputs will not actually affect the outcome
    print ("You have reached", word1 ,"junction.\nDo you want to turn left (L), turn right (R) or go straight ahead(S)?")
    turning = input().lower()
    #This is a simple instruction that means that the first time you come to a junction, it will say 'a junction' but the second time it will say 'another junction'
    word1 = "another"
    #This 'if' statement means that the program will only continue if the user has inputed the letters 'L', 'R' or 'S'
    while turning not in ["l","r","s"] :
        time.sleep (0.7)
        print ("Sorry, I didn't understand that")
        turning = input().lower()
    choice = randint (1,10)
    #This is just going to display a random message which will affect the outcome
    time.sleep (1)
    if choice == 1:
        print ("You have found the exit!")
        return shield1, word1, True
    elif choice == 2:
        print ("You have found a shield!")
        time.sleep(1)
        shield1 = shield1 +1
        return shield1, word1,False
    elif choice == 3:
        print ("You have found two shields!")
        time.sleep(1)
        shield1 = shield1 +2
        return shield1, word1,False
    elif choice == 4:
        print ("You have found three shields!")
        time.sleep(1)
        shield1 = shield1 +3
        return shield1, word1,False
    elif choice == 5:
        print ("A fairy has jumped into your pants!")
        time.sleep(2)
        print ("You lose two shields")
        time.sleep(1)
        shield1 = shield1 -2
        return shield1, word1,False
    elif choice == 6:
        treasurechest(shield1)
        return shield1, word1,False
    elif choice == 7:
        print ("You have tripped over a log!")
        time.sleep(2)
        print ("You lose a shield")
        time.sleep(1)
        shield1 = shield1 -1
        return shield1, word1,False
    elif choice == 8:
        print ("An angry teenager is staring at you in the eye.")
        time.sleep(2.5)
        print ("He uses laziness...")
        time.sleep(1.5)
        print ("It's super effective!")
        time.sleep(1)
        print ("You lose three shields")
        time.sleep(1)
        shield1 = shield1 -3
        return shield1, word1,False
    elif choice == 9:
        print ("You have encountered an ogre...")
        time.sleep(1.5)
        print ("He bashes you over the head with a steel bar")
        time.sleep(2)
        print ("You lose two shields")
        time.sleep(1)
        shield1 = shield1 -2
        return shield1, word1,False
    else:
        print ("A goblin aproaches and says the following:")
        time.sleep(2)
        goblin(shield1)
        return shield1, word1,False

    def goblin(shield):
        time1 = [1,2.5,1,1,1]
        text = ["'Do you want to play my magical roulette?\n There are three different outcomes:'",
                "You lose a shield", "You gain a shield","Nothing happens"]
        print_on_a_timer(time1,text)
        goblin = 0
        while goblin == 0:
            print ("Do you want to play? Y or N?")
            choice2 = input().lower()
            time.sleep(1)
            if choice2 not in ["y","n"]:
                print ("Sorry I didnt understand that")
            elif choice2 not in ["y"]:
                print ("Okay bye")
                TakeTurn()
            else:
                print ("Let's play!")
                time.sleep(1)
                print ("Spinning...")
                time.sleep(1)
                print ("Spinning...")
                time.sleep(1)
                print ("Spinning...")
                time.sleep(1)
                roulette = randint (1,3)
                if roulette == 1:
                    print ("Nothing happens")
                    goblin = 1
                elif roulette == 2:
                    print ("Im going to have to take one of your shields")
                    shield = shield -1
                    goblin = 1
                else:
                    print ("Here! Have a shield!")
                    shield = shield +1
                    goblin = 1

def treasurechest(shield):
    treasure = 1
    while treasure == 1:
        print ("You have found a treasure chest! Do you want to open it? Y or N?")
        chest = input().lower()
        if chest not in ["y","n"]:
            print ("Sorry, I didn't understand that")
        elif chest not in ["y"]:
            print ("Okay Bye")
            treasure = 0
        else:
            time.sleep(1)
            print ("Opening...")
            time.sleep(1)
            print ("Opening...")
            time.sleep(1)
            print ("Opening...")
            time.sleep(1)
            chest = randint (1,6)
            if chest == 1:
                print ("You have found a shield!")
                shield = shield +1
                treasure = 0
            elif chest == 2:
                print ("You have found two shields!")
                shield = shield +2
                treasure = 0
            elif chest == 3:
                print ("A dwarf jumps out and steals one of your shields!")
                shield = shield -1
                treasure = 0
            elif chest == 4:
                print ("An evil fairy steals two of your shields!")
                shield = shield -2
                treasure = 0
            elif chest == 5:
                print ("Sorry, the chest is empty")
                treausre = 0
            else:
                print ("A goblin is in the chest and says the following...")
                time.sleep(2)
                goblin()

def print_on_a_timer(times, lines):
    for times, lines in zip(times, lines):
        time.sleep(times)
        print(lines)


main(shield,word)
