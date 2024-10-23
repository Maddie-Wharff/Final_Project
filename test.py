reveal = "_ _ _ _ _ _ _ _ _ _ _"
print("This is Hangman!\n_______\n O     |\n-|-    |\n ^     |")
print("This is the word you need to guess!\n", reveal)
  
guess = input("Give me a letter: \n")

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
        print("P is the sixth and seventh letter!")
elif guess == "a":
        print("A is the eighth letter!")
elif guess == "b":
        print("B is the ninth letter!")
elif guess == "l":
        print("L is the tenth letter!")
elif guess == "e":
        print("E is the eleventh letter!")
else:
        print("There are no", guess)