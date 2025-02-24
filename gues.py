import random
import os
guess = random.randint(1, 100)
userGuess = []
guessCount = 0
guessLimit = 3
gameTrial = False

def game():
    while userGuess != guess and gameTrial != True:
        try:
            if guessCount < guessLimit:
                userGuess = int(input("User Guess : "))
                guessCount += 1
            else:
                gameTrial = True
        except:
            raise ValueError("INVALID DATA INPUT ", os.strerror(""))

##def retry(): 
if gameTrial:
    print("You're a dummy")
    print("You lost \nLucky Number is : ", guess)
else:
    print("You Won")   
##        print("Do you wanna challenge me again???..")
##        choice = input("Yes/No :"  )
##        if choice == "Yes" or choice == "YES" or choice == "Y" or choice == "y":
##            print("GoodLuck ")
##            game()
##        elif choice == "NO" or choice == "no" or choice == "N" or choice == "n":
##            print("Why be such a coward")
##        else:
##            print("Not a choice")

