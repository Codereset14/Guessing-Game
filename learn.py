import random
from time import sleep

comp_guess = random.randint(1, 100)



def guess():
    i = 5
    while i > 0:
        print("You have " + str(i) + " Chances left!")
        sleep(0.4)
        user_guess = int(input(("What number am I thinking about?   ")))

        if user_guess == comp_guess:
            print("You got it!, the number was " + str(comp_guess))

        elif user_guess > comp_guess:
            print("Too high, try again!")
            sleep(1)
            
                    
                
        elif user_guess < comp_guess:
            print("Too low, try again!")
            sleep(1)
        i -= 1
        
        if i == 0:
            print("You have reached the max amount of trials!")
            sleep(0.3)

        





print("Loading game...")
sleep(2)

print("WELCOME TO NATHAN'S GUESSING GAME!")
sleep(4.5)

print("In this game, the computer is currently thinking of a number and it's your duty to guess that number!")
sleep(3.5)
choice = input("Would you like to go on with this challenge? y/n:     ")


if choice == "y":
    sleep(0.5)
    print("Very well then!")
    sleep(1.5)
    guess()
elif choice == "n":
    print("Alright then, till next time my friend.")



