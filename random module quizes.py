import random
fruit = ["mango", "apple", "oranges"]
print(random.choice(fruit))

headAndTail = random.choice(["H", "T"])
choice = input("Enter your choice: ").upper()
if choice == headAndTail:
    print("YOU WIN")
else:
    print("YOU LOST")

num = random.randint(0,5)
guesslimit = 3
guesscount = 0
userguess = []
game = False

while userguess != num and game != True:
    if guesscount < guesslimit:
        userguess = int(input("Guess : "))
        guesscount += 1       
    else:
        game = True
        
if game:
    print("You lost \nLucky Number is : ",num)
    print("Try Again... Dummy!!")
else:
    print("YOU WIN")

