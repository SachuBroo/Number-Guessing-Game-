#number guessing game

import random
number = random.randint(10,50)
guess = 0
while guess<5:
    choice = int(input("Choose a number between 10 and 50:"))
    if choice < 10 or choice > 50:
        print("Invalid input, please choose a number between 10 and 50")
        continue
    elif choice == number:
        print("You win!!")
        break
    else:
        print("Try again!")
        guess += 1

if not guess < 5:
    print(f"\n 0 attempts left, you lose!!, The number was {number}")