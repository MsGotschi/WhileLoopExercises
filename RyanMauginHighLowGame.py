# Ryan Maugin
# 23/10/16
# Guess the number the computer is thinking

from random import randint

randomNumber = randint(0, 100)
guess = False
chance = 0

while not guess:
    try:
        guessNumber = int(input("Enter your guess: "))

        if chance == 6:
            print("You lost your 6 chances the number was {}".format(randomNumber))
            quit()

        if guessNumber < randomNumber:
            print("Higher")
            chance += 1
        elif guessNumber > randomNumber:
            print("Lower")
            chance += 1
        elif guessNumber == randomNumber:
            print("You guess correctly!")
            quit()
    except ValueError:
        print("Invalid inout, try again!")
