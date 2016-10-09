#Chayann Bradford
#7th October 2016
#While Loops

"""
a)Write a WHILE loop that continually asks a user to enter a character and stops when the user pressed the 'x'
b)Write a WHILE loop that keeps adding up numbers the user enters until the sum of the numbers is > 100
c)Using random numbers, loops and IF statements write a game that

1) Picks a number between 1 and 100
2) Asks the user to guess
3) tells the user whether they are too high, too low or have guessed the secret number
4) Gives the user 6 chances
5) Tells the user at the end what the secret number was only if they have NOT guessed
it correctly (ie they have not won)
"""

#a)Write a WHILE loop that continually asks a user to enter a character and stops when the user pressed the 'x'

"""
userCh=input("please enter a character, 'x' to exit ").lower()
while userCh != 'x':
    userCh = input("please enter a character, 'x' to exit").lower()
"""

#b)Write a WHILE loop that keeps adding up numbers the user enters until the sum of the numbers is > 100


sum= 0
while sum <= 100:
        num= int(input("Please enter a number:"))
        sum = sum+num

else:
    print('Your number is greater than 100!')


#c)Using random numbers, loops and IF statements write a game that

"""
from random import randint

chance= 0
won=False
secretnumber= randint(1,100)
print(secretnumber)

while chance <6 and not won:

    guess = int(input('Please guess a number:'))  # validate

    if guess < secretnumber:
        print('too low')
    elif guess > secretnumber:
        print('too high')
    else:
        print('you guessed it! ')
        won =
"""





