import random
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\nLet's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_score += 1
            print("You win!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
