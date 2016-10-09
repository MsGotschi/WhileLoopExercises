# Write a WHILE loop that continually asks a user to enter a character and stops when the user pressed the 'x'

Program=True
while Program == True:
    x=input("Input a character, or enter 'x' to end the program: \n >")
    if x == 'x':
        Program = False
        break
