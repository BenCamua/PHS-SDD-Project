Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> UserName = input('Hello young traveller may I ask what is your name: ')
print('So your name is ' + UserName + '? What a wonderful name for our next lengendary warrior!')
invalid_input = True
def WarriorQuestion():
  Join = input('You want to become a warrior right? Yes or No: ') .lower()
if Join.startswith('y'):
   print("Great, welcome to the game called Eindhoven " + UserName + '!')
   invalid_input = False 
elif Join.startswith('n'):
      print ("Sorry for asking dickhead, no one needed you anyways comeback when you are ready.")
      invalid_input = False 
else:
      print ("Sorry, that was an invalid command!")
      invalid_input = False 
WarriorQuestion()
