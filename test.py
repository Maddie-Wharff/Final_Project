print("This is Hangman!\n_______\n O     |\n-|-    |\n ^     |\n____________")
print("This is the word you need to guess!\n _ _ _ _ _ _ _ _ _ _ _")
word = ["u", "n", "s", "t", "o", "p", "a", "b", "l", "e"]
  
guess = input("Give me a letter: \n")

reveal = "_ _ _ _ _ _ _ _ _ _ _"

for let in word:
    if guess == "u":
        print("U is the first letter!")
    elif guess == "n":
        print("N is the second letter!")
    elif guess == "s":
        print("S is the thrid letter!")
    elif guess == "t":
        print("T is the fourth letter!")
    elif guess == "o":
        print("O is the fifth letter!")
    elif guess == "p":
        print("Yes it has a ", guess)








name = input("enter a name ")
namedos = input("enter a second name ")
place = input("enter a place ")
verb = input("enter a verb ")
print(name + " and " + namedos + " went to " + place + " so they could " + verb + ".")

