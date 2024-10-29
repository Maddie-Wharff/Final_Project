#Hangman by Michael Willes, Maddie Wharff, Elora Anderson, and Cephas Petersen

#Variables - All
import random
wordList = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "jump", "dog", "play" , "fox", "umbrella", "chair", "cooking", "night", "hungry", "orange", "ghost", "people", "pumpkin", "holiday", "phone", "joke"]
word = ""
points = 0
usedLetters = []
displayWord=""
#function to set everything to 0 - Cephas and Michael
def restart():
  global word
  global wordList
  global usedLetters
  word = random.choice(wordList)
  points = 0
  usedletters= []
  usedLetters.clear()
restart()
#functions to let the user win / lose - Cephas
def winGame():
  print("Congrats you win!!!")
  winRestart = input("if you would like to restart press 1:")
  if winRestart =="1":
    restart()
    runGame()
  else:
    winGame()


def failGame():
  print("you have failed 6 times you are dead")
  failRestart = input("if you would like to restart press 2:")
  if failRestart=="2":
    restart()
    runGame()
  else:
    failGame()
#function to let the user guess - Maddie
def guess():
  choice = input("guess a letter: ").strip().lower()
  usedLetters.append(choice)
  if choice not in word:
    global points
    points += 1
#make the hangman - Elora
def hangman():
  if points == 0:
    print("_______")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("---------")
  elif points == 1:
    print("_______")
    print(" 0    |")
    print("      |")
    print("      |")
    print("      |")
    print("---------")
  elif points == 2:
    print("_______")
    print(" 0    |")
    print(" |    |")
    print("      |")
    print("      |")
    print("---------")
  elif points == 3:
    print("_______")
    print(" 0    |")
    print("/|    |")
    print("      |")
    print("      |")
    print("---------")
  elif points == 4:
    print("_______")
    print(" 0    |")
    print("/|\\   |")
    print("      |")
    print("      |")
    print("---------")
  elif points == 5:
    print("_______")
    print(" 0    |")
    print("/|\\   |")
    print("/      |")
    print("      |")
    print("---------")
  elif points == 6:
    print("_______")
    print(" 0    |")
    print("/|\\  |")
    print("/ \\  |")
    print("      |")
    print("---------")
#function to replace letters with blanks - Maddie & Michael
def display():
  displayWord=""
  for x in word:
    if x in usedLetters:
      displayWord= displayWord+x
    else:
      displayWord=displayWord+"_"
  print(displayWord)
  if displayWord == word:
    winGame()
# function to run game.-Maddie and Elora
# call every function - All
# plus some extra stuff! - Michael
def runGame():
  global points
  global usedLetters
  global word
  global displayWord
  hangman()
  display()
  for i in range(len(usedLetters)):
    print(str(i+1) + "." + (usedLetters[i]))
  guess()
  if points == 6:
    print("the word was: "+ word)
    hangman()
    failGame()
  else:
      runGame()
runGame()