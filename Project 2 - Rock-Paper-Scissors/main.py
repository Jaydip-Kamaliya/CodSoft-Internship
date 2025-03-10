import random

print("\n=== Rock, Paper, Scissors Game ===\n")
print("Notes:")
print("- Type 'quit' to quit the game.")
print("- Valid Inputs : rock, paper, scissors or quit")
print("- The final score will be shown after quitting the game.")

guess = {
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}

valid_guess = ["scissors", "paper", "rock"]

# Initialize scores and counters
computer_score = 0    # Score of the computer
user_score = 0        # Score of the user
total_rounds = 0      # Total number of rounds played
draw = 0              # Number of draws

# Main game loop
while True: 

    # Computer makes a random guess
    computer_int = random.randint(1, 3)
    computer_guess = guess[computer_int]

    user_guess = input("\nEnter your guess: ").strip().lower()

    # Check if the user wants to quit the game
    if user_guess == "quit":
        if computer_score == 0 and user_score == 0:
            break
        else:
            print()
            print("{:<15} - {}".format("Computer score", computer_score))
            print("{:<15} - {}".format("Your score", user_score))
            print("{:<15} - {}".format("Draw", draw))
            print("="*20)
            print("{:<15} - {}".format("Total Rounds", total_rounds))
            
            if computer_score > user_score:
                print("\nThe computer wins. Better luck next time!\n")
            elif computer_score == user_score:
                print("\nIt's a tie overall! Great match!\n")
            else:
                print("\nCongratulations! You're the winner!\n")
            break 

    # Check if the user input is valid
    elif user_guess not in valid_guess:
        print("Plese Enter a valid guess")
        continue
    
    # Check who wins
    elif computer_guess == "rock" and user_guess == "scissors":
        print("Computer wins this round")
        computer_score += 1
    elif computer_guess == "paper" and user_guess == "rock":
        print("Computer wins this round")
        computer_score += 1
    elif computer_guess == "scissors" and user_guess == "paper":
        print("Computer wins this round")
        computer_score += 1
    elif computer_guess == user_guess:
        print("It's a Draw")
        draw += 1
    else:
        print("You win this round")
        user_score += 1
    total_rounds += 1

    print(f"Computer guessed - {computer_guess}")