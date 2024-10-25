# Hangman, by Elora, Maddie, Cephas, and Michael
        
# Pick a word/ start the game - Michael
import random
wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "the", "dog", "in" , "fox"]
word = ""
wordGuess = ""
points = 0
def gameStart():
        global wordlist
        global word
        global wordGuess
        score = 0
        wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "the", "dog", "in" , "fox"]
        word = random.choice(wordlist)
        wordGuess = ""
        game()


# Let them pick a letter - All
guess = input("Give me a letter: \n")

# If they were wrong print a part of the man - Elora, Cephas
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


# Check if letter is in word - Maddie    
if guess in word:
        print("Correct!")
else:
        print("Incorrect :(")
        points = points + 1
        hangman()
        

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
        game()