from Blackjack_logo import blackjack_logo
import random
import os
import platform


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def deal_card():
    """Returns a random card from the dictionary"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, com_score):
    if user_score > 21 and com_score > 21:
        return "You went over. You lose."
    
    if user_score == com_score:
        return "It's a tie."
    elif com_score == 0:
        return "You win, the computer busted."
    elif user_score > 21:
        return "You lose."
    elif com_score > 21:
        return "You win, the computer busted."
    elif user_score > com_score:
        return "You win."
    else:
        return "You lose."
    

def play_blackjack():

    print(blackjack_logo)

    user_cards= []
    com_cards= []
    is_game_over= False

    for _ in range(2):
        user_cards.append(deal_card())
        com_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        com_score = calculate_score(com_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {com_cards[0]}")

        if user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Do you want to hit or stand? (h/s): ")
            if choice.lower() == "h":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while com_score != 0 and com_score < 17:
        com_cards.append(deal_card())
        com_score = calculate_score(com_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {com_cards}, final score: {com_score}")
    print(compare(user_score, com_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y" :
    clear()
    play_blackjack()