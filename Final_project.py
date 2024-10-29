# Hangman, by Elora, Maddie, Cephas, and Michael

# Pick a word/ start the game - Michael
import random
wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "jump", "dog", "play" , "fox", "umbrella", "chair", "cooking", "night", "hungry", "orange", "ghost", "people", "pumpkin", "holiday", "phone", "joke"]
word = ""
wordGuess = ""
points = 0

def ask():

        guess = input("give me a letter:\n")
        if guess in word:
                      print("Correct!")
        else:
          print("Incorrect :(")
          points =+ 1
                #TY
def hangman():
        global points
        if points == 0:
                print("\n----\n   |n|\n|\n|\n|\n|\n|\n--------")
        elif points ==1:
                print("\n-----\n|   |\n|   0\n|\n|\n|\n|\n|\n|\n-------")
        elif points ==2:
                print("\n-----\n|   |\n|   0\n|   -+-\n|\n|\n|\n|\n|\n-------")
        elif points ==3:
                print("\n-----\n|   |\n|   0\n| /-+-\n|\n|\n|\n|\n|\n-------")
        elif points ==4:
                print("\n-----\n|   |\n|   0\n| /-+-\ \n|\n|\n|\n|\n|\n-------")
        elif points ==5:
                print("\n-----\n|   |\n|   0 \n| /-+-\ \n|   |\n|\n|\n|\n|\n-------")
        elif points ==6:
                print("\n-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|\n|\n|\n-------")
        elif points ==7:
                print("\n-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |\n|\n|\n-------")
        elif points ==8:
                print("\n-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |\n|  |\n|\n-------")
        elif points ==9:
                print("\n-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |  |\n|  |\n|\n-------")
        elif points ==10:
                print("\n-----\n|   |\n|   0\n| /-+-\ \n|   |\n|   |\n|  |  |\n|  |  |\n|\n-------")

def game():
        hangman()
        ask()
        gameEnd()

def gameStart():
        global wordlist
        global word
        global wordGuess
        score = 0
        wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "jump", "dog", "play" , "fox", "umbrella", "chair", "cooking", "night", "hungry", "orange", "ghost", "people", "pumpkin", "holiday", "phone", "joke"]
        word = random.choice(wordlist)
        wordGuess = ""
        game()
        #sounds good
#I am going to make another p[age for the code I used before ok!
for letter in word:
        print("_")

# Let them pick a letter - All

# If they were wrong print a part of the man - Elora, Cephas



# Check if letter is in word - Maddie    

        
# End the game - Michael
def gameEnd():
        if wordGuess == word:
                question = input(" Congratulations!\n you won!\n Would you like to restart?\n if so press y").strip().lower()
                if question =="y":
                        gameStart()
                else:
                        gameEnd
        elif points ==10:
                question == input(" Woops the word was {word}\n you lost.\n Would you like to restart?\n if so press y").strip().lower()
                if question =="y":
                        gameStart()
                else:
                        gameEnd

while true:
        gameStart()

 