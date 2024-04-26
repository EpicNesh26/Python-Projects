print("Idea:We import a random number and ask the user to guess the number and tell them if they were above or below the guessed number")
print()

import random 

nr = input("Type a number")
if nr.isdigit:
    nr=int(nr)

    if nr <= 0:
        print('Please type a number larger than 0')
        quit()
else:
    print('Please type a number next time')
    quit()

random_number=random.randint(0,nr)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    
    if user_guess > random_number:
        print("You were above the number")
    elif user_guess < random_number:
        print("You were below the number")
    else:
        print("You got it")
        print("You got it in ",guesses ,"Guesses")
        break



