from game_art import logo, vs
from game_data import data
import random
import os
import platform

def clear_screen():
    """Clears screen"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_random_data():
    """"Get random data from game_data"""
    return random.choice(data)


def display_data(option):
    """It displays data the selected randomly from the game_data"""
    name = option["name"]
    description = option["description"]
    country = option["country"]
    return f"{name} a {description} from {country}"


def check_answer(f_follower, s_follower, instance):
    if f_follower > s_follower:
        return instance == "A"
    else:
        return instance == "B"


def play_game():
    score = 0
    first_account = get_random_data()
    second_account = get_random_data()
    game_continue = True

    print(logo)
    print("Welcome to the Higher or Lower Game!")
    print("Guess who has more followers!")

    while game_continue:
        first_account = second_account
        second_account = get_random_data()
        if first_account == second_account:
            second_account = get_random_data()
            continue
        print(f"Compare A: {display_data(first_account)}.")
        print(vs)    
        print(f"Compare B: {display_data(second_account)}.")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        first_follower_count = first_account["follower_count"]
        second_follower_count = second_account["follower_count"]
        is_correct = check_answer(first_follower_count, second_follower_count, user_guess)
        clear_screen()

        if is_correct:
            print("You're right!")
            score += 1
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


play_game()