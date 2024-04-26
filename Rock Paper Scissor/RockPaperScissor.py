print("Idea:Make it so that computer keeps track on how many times the computer wins and how many times the user wins")

import random

user_wins=0
computer_wins=0

options=["rock","paper","scissor"]

while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit  : ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number=random.randint(0,2)

    computer_pick=options[random_number]
    print("Computer picker ",computer_pick + ".")
    print()

    if user_input =="rock" and computer_pick =="Scissor":
        print("You won!")
        user_wins+=1
        print()

    elif user_input =="rock" and computer_pick =="rock":
        print("Its a tie")
        print()

    elif user_input =="paper" and computer_pick =="rock":
        print("You won!")
        user_wins+=1
        print()

    elif user_input =="paper" and computer_pick =="paper":
        print("Its a tie")
        print()

    elif user_input =="scissor" and computer_pick=="paper":
        print("You won!")
        user_wins+=1
        print()

    elif user_input =="scissor" and computer_pick=="scissor":
        print("Its a tie")
        print()

    else:
        print("You lost!")
        computer_wins+=1

print("You won",user_wins,"times")
print("The computer won ",computer_wins,"times")
print("Thank you for playing!")