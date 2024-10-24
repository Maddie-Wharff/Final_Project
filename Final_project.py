# By Elora, Maddie, Cephas, and Michael

#extremely important things that I am adding!
def gameEnd():
        if wordGuess = word:
                question = input(" Congratulations!\n you won!\n Would you like to restart?\n if so press y").strip().lower()
                if question = "y":
                        gameStart()
                else:
                        gameEnd
        elif score = 6:
                question = input(" Woops the word was {word}\n you lost.\n Would you like to restart?\n if so press y").strip().lower()
                if question = "y":
                        gameStart()
                else:
                        gameEnd
        game()
        
# Pick a word - Both
import random
wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "the", "dog", "in" , "fox"]
word = ""
wordGuess = ""
score = 0
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

# Check if letter is in word - Maddie    
if guess in word:
        print("Correct!")
else:
        print("Incorrect :(")

# If they were wrong print a part of the man - Elora

def hangman(): 
        
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

# End the game - Michael