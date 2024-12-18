import random

print("Rock Paper Scissors")
choices = ["rock", "paper", "scissors"]

# Get user input
try:
    user_choice = int(input("What is your choice? Enter 0 for rock, 1 for paper, 2 for scissors: "))
    if user_choice not in [0, 1, 2]:
        raise ValueError("Invalid choice. Please enter 0, 1, or 2.")
except ValueError as e:
    print(e)
    exit()

# Generate computer choice
computer_choice = random.randint(0, 2)

# Display choices
print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}.")

# Determine winner
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice - computer_choice) % 3 == 1:
    print("You win!")
else:
    print("Computer wins!")
