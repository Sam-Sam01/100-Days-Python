from art import gtn_logo
import random


EASY_LEVEL = 10
HARD_LEVEL = 5


def set_level(level):
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    else:
        print("Invalid level. Default to 'easy'.")
        return EASY_LEVEL


def check_answer(result, estimate, spin):
    if estimate > result:
        print("Too high! Try again.")
        return spin - 1
    elif estimate < result:
        print("Too low! Try again.")
        return spin - 1
    else:
        print("Congratulations! You've guessed the number correctly.")


def game():
    print(gtn_logo)
    print("Welcome to the NUMBER GUESSING GAME!")
    print("I will generate a random number between 1 and 100 for you.")
    answer = random.randint(1, 100)
    print("%d" % answer)
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").strip().lower()
    turns = set_level(difficulty)
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: ").strip())

        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Keep trying!")

game()
