#Mohammed Shekh
#09/10/2016
#While Loops Exercise H/W (Due: 10/10/2016)

print("\nTask 1: ----------------------------------\n")
UserInput=False
while UserInput == False:
    ask = input("Enter any character ('x' to quit)").lower()
    if ask == 'x':
        UserInput=True
        break
    else:
        continue

print("\nTask 2: ----------------------------------\n")
Total=False
while Total == False:
    print("Start now/again:")
    ask = int(input("Enter a number: "))
    added_up=False
    if ask >= 100 or added_up == True:
        Total=True
    elif ask < 100 or added_up ==False:
        ask_2 = int(input("Not enough, enter another number: "))
        sum_of_all=ask + ask_2
        if sum_of_all >= 100:
            break
        else:
            continue
    else:
        continue

print("\nTask 3: ----------------------------------\n")
import random
set_number=random.randint(1, 101)
print("")
chance=0
print("Hi! Guess the number the computer selected between 1 to 100.\nYou have 6 chances. Good luck!")
while chance < 6:
    q=int(input("Guess the number: "))
    if q == set_number:
        print("OMG! You are right. Well done!")
        break
    elif q < set_number:
        print("Too Low.")
        chance+=1
    elif q > set_number:
        print("Too High.")
        chance += 1
    else:
        error=input("There's been some kind of ERROR. Please run the program again. Thank you!")
        break
print("\nThe number was", set_number)