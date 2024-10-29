#Hangman by Michael Willes, Maddie Wharff, Elora Anderson, and Cephas Petersen
import random
wordlist = ""
word = ""
points = 0
usedLetters = [""]
displayWord = ""
end = 0
def loseGame():
    question = input("Oh no! You lost! Would you like to try again?\n If so type y.\n").strip().lower()
    if question == "y":
        end = 1
    else:
       loseGame()
# \ \n \\
def gallows():
  global points
  if points == 0:
    print("_______")
    print(" |     ")
    print(" |")
    print(" |")
    print(" |")
    print("---------")
  elif points == 1:
    print("_______")
    print(" |    0")
    print(" |")
    print(" |")
    print(" |")
    print("---------")
  elif points == 2:
    print("_______")
    print(" |    0")
    print(" |    |")
    print(" |")
    print(" |")
    print("---------")
  elif points == 3:
    print("_______")
    print(" |    0")
    print(" |   /|")
    print(" |")
    print(" |")
    print("---------")
  elif points == 4:
    print("_______")
    print(" |    0")
    print(" |   /|\\")
    print(" |")
    print(" |")
    print("---------")
  elif points == 5:
    print("_______")
    print(" |    0")
    print(" |   /|\\")
    print(" |   /")
    print(" |")
    print("---------")
  elif points == 6:
    print("_______")
    print(" |    0")
    print(" |   /|\\")
    print(" |   / \\")
    print(" |")
    print("---------")
    loseGame()
#def hangman():
    #global points
    #if points == 0:
        #print("\n----\n   |n|\n|\n|\n|\n|\n|\n--------")
    #elif points ==1:
        #print("\n----\n|   |\n   0\n|\n|\n|\n|\n|\n|\n-------")
    #elif points ==2:
       # print("\n-----\n|   |\n|   0\n|   -+-\n|\n|\n|\n|\n|\n-------")
    #elif points ==3:
    #    print("\n-----\n|   |\n|   0\n| /-+-\n|\n|\n|\n|\n|\n-------")
    #elif points ==4:
    #    print("\n-----\n|   |\n|   0\n| /-+-\\ \n|\n|\n|\n|\n|\n-------")
    #elif points ==5:
    #    print("\n-----\n|   |\n|   0 \n| /-+-\\ \n|   |\n|\n|\n|\n|\n-------")
    #elif points ==6:
     #   print("\n-----\n|   |\n|   0\n| /-+-\\ \n|   |\n|   |\n|\n|\n|\n-------")
    #elif points ==7:
    #    print("\n-----\n|   |\n|   0\n| /-+-\\ \n|   |\n|   |\n|  |\n|\n|\n-------")
   # elif points ==8:
       # print("\n-----\n|   |\n|   0\n| /-+-\\ \n|   |\n|   |\n|  |\n|  |\n|\n-------")
    #elif points ==9:
        #print("\n-----\n|   |\n|   0\n| /-+-\\ \n|   |\n|   |\n|  |  |\n|  |\n|\n-------")
  #  elif points ==10:
       # print("\n-----\n|   |\n|   0\n| /-+-\\ \n|   |\n|   |\n|  |  |\n|  |  |\n|\n-------")
        #loseGame()


def win_game():
    global end
    question = input("congrats! You have won would you like to play again?\n if so press y").strip().lower()
    if question == "y":
        end = 1


def spaceDisplay():
    global word
    global usedLetters
    global displayWord
    for x in word:
        if x in usedLetters:
            displayWord= displayWord+x
        else:
            displayWord=displayWord+"_"
        print(displayWord)
        if displayWord == word:
            win_game()

def gameAsk():
    choice = input("guess a letter: ").strip().lower()
    usedLetters.append(choice)
    if choice not in word:
      global points
      points += 1

# ok things to do: make the gallows and everything above this def. statement"^" yes you can copy and  paist
def gameStart():
    wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "jump", "dog", "play" , "fox", "umbrella", "chair", "cooking", "night", "hungry", "orange", "ghost", "people", "pumpkin", "holiday", "phone", "joke"]
    word = random.choice(wordlist)
    points = 0
    usedLetters = [""]
    displayWord = ""
    end = 0
    game()



#These are the three things we need to do
def game():
    while True:
        gallows()
        spaceDisplay()
        gameAsk()
        for i in range(len(usedLetters)):
            print(str(i) + "." + (usedLetters[i]))
        if end == 1:
            end == 0
            break
            gameStart()
               

gameStart()