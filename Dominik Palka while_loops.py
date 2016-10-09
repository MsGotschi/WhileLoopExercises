def game1():
    user= False
    while user==False:
        usernumber=input("please enter a character")
        if usernumber=="x" or usernumber== "X":
            user=True
            print("the program will now exit")
            exit()


#game1()

def game2():
    count=0
    while count <100:
        userinput=int(input("please input a number"))
        count+=userinput
        print("the current total is",count)
        
#game2()

import random
pcchoice=random.randint(1,101)
def game3():
    userchoice=int(input("Please guess the number the computer picked form 1 to 100"))
    while userchoice >=1 and userchoice <=100:
        if userchoice == pcchoice:
            print("well done you guess right")
            exit()
        elif userchoice > pcchoice:
            print("guess again your number too big")
            game3()
        elif userchoice <pcchoice:
            print("guess again number too small")
            game3()
        else:
            print(error)
            game3()
            

game3()

            
        
    
    
    
    




    

            
        
        
    
    
    
