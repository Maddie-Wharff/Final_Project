#Hangman by Michael Willes, Maddie Wharff, Elora Anderson, and Cephas Petersen

#Variables - All
import random
wordList = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "jump", "dog", "play" , "fox", "umbrella", "chair", "cooking", "night", "hungry", "orange", "ghost", "people", "pumpkin", "holiday", "phone", "joke"]
word = ""
points = 0
usedLetters = []
displayWord=""
#function to set everything to 0 - Cephas & Michael
def restart():
  global word
  global wordList
  global points
  global usedLetters
  word = random.choice(wordList)
  points = 0
  usedletters= []
  usedLetters.clear()
restart()
#function to let the user win - Cephas
def winGame():
  print("Congrats you win!!!")
  winRestart = input("if you would like to restart press 1:")
  if winRestart =="1":
    restart()
    runGame()
  else:
    winGame()
#function to let the user lose - Cephas
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
#make the gallows - Elora
def gallows():
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
#function to run game.-all \\\ call every function-all \\\plus some extra stuff! - Michael
def runGame():
  global points
  global usedLetters
  global word
  global displayWord
  gallows()
  display()
  for i in range(len(usedLetters)):
    print(str(i+1) + "." + (usedLetters[i]))
  guess()
  if points == 6:
    print("the word was: "+ word)
    gallows()
    failGame()
  else:
      runGame()
runGame()