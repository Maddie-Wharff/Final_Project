#Hangman by Michael Willes, Maddie Wharff, Elora Anderson, and Cephas Petersen


import random
wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "jump", "dog", "play" , "fox", "umbrella", "chair", "cooking", "night", "hungry", "orange", "ghost", "people", "pumpkin", "holiday", "phone", "joke"]
word = ""
points = 0
usedLetters = []
displayWord=""
#functoin hung a conditional that checks failed attempts to see how much of the gallows is drawn
def restart():
  global word
  global wordlist
  global fails
  global used_letters
  word = random.choice(words_to_chose)
  fails = 0
  used_letters= [""]
restart()
def win_game():
  print("Congrats you win!!!")
  win_restart = input("if you would like to restart press 1:")
  if win_restart =="1":
    restart()
    run_game()
  else:
    win_game()
def gallows():
  if fails == 0:
    print("_______")
    print(" |     ")
    print(" |")
    print(" |")
    print(" |")
    print("---------")
  elif fails == 1:
    print("_______")
    print(" |    0")
    print(" |")
    print(" |")
    print(" |")
    print("---------")
  elif fails == 2:
    print("_______")
    print(" |    0")
    print(" |    |")
    print(" |")
    print(" |")
    print("---------")
  elif fails == 3:
    print("_______")
    print(" |    0")
    print(" |   /|")
    print(" |")
    print(" |")
    print("---------")
  elif fails == 4:
    print("_______")
    print(" |    0")
    print(" |   /|\\")
    print(" |")
    print(" |")
    print("---------")
  elif fails == 5:
    print("_______")
    print(" |    0")
    print(" |   /|\\")
    print(" |   /")
    print(" |")
    print("---------")
  elif fails == 6:
    print("_______")
    print(" |    0")
    print(" |   /|\\")
    print(" |   / \\")
    print(" |")
    print("---------")
#function blanks for loop that checks to see if each letter in the word is in our guessed letters list if in list display it, if not display an underscore
def display():
  display_word=""
  for x in word:
    if x in used_letters:
      display_word= display_word+x
    else:
      display_word=display_word+"_"
  print(display_word)
  if display_word == word:
    win_game()
#function to run game. call the function for the gallows, call function for the blanks, display guessed letters, create a variable for the user to input to let them guess a letter, check if the letter is in the word, if not add it to the failed attempts by one. add letter to the guessed letters.
def run_game():
  global fails
  global used_letters
  global word
  global display_word
  gallows()
  display()
  for i in range(len(used_letters)):
    print(str(i+1) + "." + (used_letters[i]))
  def guess():
    choice = input("guess a letter: ").strip().lower()
    used_letters.append(choice)
    if choice not in word:
      global fails
      fails += 1
  guess()
  def fail_game():
    print("you have failed 6 times you are dead")
    fail_restart = input("if you would like to restart press 2:")
    if fail_restart=="2":
      restart()
      run_game()
    else:
      fail_game()
  if fails == 6:
    print("the was: "+ word)
    gallows()
    fail_game()
  else:
    run_game()
run_game()


#check to see if the game ends!!! allow player to restart if they want.

#function that restarts everything: pick random word and reset all variables