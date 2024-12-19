import random
import word_list 
from hangman_graphics import stages, logo
import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


chosen_word = random.choice(word_list.word_list)
print(logo)
print("Welcome to Hangman!")

lives = len(stages) - 1
end_of_game = False
display = []
word_len = len(chosen_word)


for letter in range(word_len):
    display += "_"
print("".join(display))

while not end_of_game:
    guess = input("Guess the letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed this {guess} letter.")

    for position in range(word_len):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess},Incorrect guess. You have {lives} lives left.")
        print(stages[len(stages)- 1- lives])

        if lives == 0:
            end_of_game = True
            print("You've lost. Better luck next time!")
            print(f"The word was: {chosen_word}")
    print("".join(display))



if "_" not in display:
    end_of_game = True
    print(f"Congratulations! You've guessed the word: {chosen_word}.")
    print("You've won!")



