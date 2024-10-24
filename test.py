import random
guess = input("What's your guess?: \n")
wordGuess = ""
word = ""
wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "the", "dog", "in" , "fox"]
score = 0
def gamestart():
        global wordlist
        global word
        global wordGuess
        score = 0
        wordlist = ["camel", "pizza", "turkey", "moon", "dream", "cat", "sweet", "tooth", "company","baboon", "gym", "belief", "leaf", "beef", "the", "dog", "in" , "fox"]
        word = random.choice(wordlist)
        
if guess in word:
        print("Correct!")
else:
        print("Incorrect :(")