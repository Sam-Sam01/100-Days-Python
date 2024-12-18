import random
from art import gtn_logo
import time

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """This function sets the difficulty of the game."""
    level = input("Select Difficulty 'Easy' or 'Hard': ").strip().lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid level. Defaulting to Easy.")
        return EASY_LEVEL_TURNS


def generate_number():
    """Generates a random number"""
    return random.randint(1, 100)


def get_valid_input():
    """This function validates user input and ensures it's an integer."""
    while True:
        try:
            num = int(input("Guess a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game(high_scores, player_name):
    print(gtn_logo)
    print(f"Welcome, {player_name}! Let's play the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = generate_number()
    attempts = set_difficulty()
    print(f"You have {attempts} attempts to guess the number.")

    start_time = time.time()
    original_attempts = attempts

    while attempts > 0:
        guess = get_valid_input()
        if guess == number_to_guess:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"Congratulations, {player_name}! You guessed the correct number in {original_attempts - attempts + 1} attempts and {elapsed_time} seconds!")

            if player_name not in high_scores or high_scores[player_name] > original_attempts - attempts + 1:
                high_scores[player_name] = original_attempts - attempts + 1
                print(f"New high score for {player_name}: {high_scores[player_name]} attempts!")
                return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}")
            elapsed_time = round(time.time() - start_time, 2)
            print(f"Time taken: {elapsed_time} seconds.")


def replay():
    return input("Do you want to play again? Type 'yes' or 'no': ").strip().lower() == "yes"


def get_player_names():
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append(name)
    return players


def main():
    high_scores = {}
    print("Welcome to the MUltiplayer Guess The Number Game!")
    players = get_player_names()

    while True:
        for player in players:
            print(f"\nIt's {player}'s turn!")
            play_game(high_scores, player)
            print("\nCurrent High Scores:")
            for name, score in high_scores.items():
                print(f"{name}: {score} attempts")

        if not replay():
            print("Thanks for playing! Final High Scores:")
            for name, score in high_scores.items():
                print(f"{name}: {score} attempts")
            break


if __name__ == "__main__":
    main()
