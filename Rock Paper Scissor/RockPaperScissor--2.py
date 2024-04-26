import random

def print_game_options():
    print("Game Options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def get_user_choice():
    user_choice = int(input("Enter your choice: "))
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please enter a valid choice.")
        return get_user_choice()
    return user_choice

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print_game_options()
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose " + ("Rock" if user_choice == 1 else "Paper" if user_choice == 2 else "Scissors"))
    print("Computer chose " + ("Rock" if computer_choice == 1 else "Paper" if computer_choice == 2 else "Scissors"))
    print(determine_winner(user_choice, computer_choice))

while True:
    play_game()
    user_response = input("Do you want to play again? Enter 'yes' or 'no': ")
    if user_response.lower() != 'yes':
        break