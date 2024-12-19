import os
import string
from graphics import display_ascii_art
from colorama import init


# Caesar Cipher encode/decode function
def caesar_cipher(text, shift, direction):
    alphabet = string.ascii_lowercase
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            base_alphabet = alphabet.upper() if is_upper else alphabet
            position = base_alphabet.index(char)
            shift_value = shift if direction == "encode" else -shift
            new_position = (position + shift_value) % len(base_alphabet)
            result += base_alphabet[new_position]
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main program loop
def main():
    while True:
        clear_screen()
        display_ascii_art()

        # User input
        direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()
        if direction not in ['encode', 'decode']:
            print("Invalid choice. Please select 'encode' or 'decode'.")
            continue

        text = input("Enter the text you want to process: ").strip()
        try:
            shift = int(input("Enter the shift number (e.g., 3): ").strip())
        except ValueError:
            print("Shift must be a valid integer. Try again.")
            continue

        # Perform the operation
        result = caesar_cipher(text, shift, direction)

        # Display the result
        print(f"\nThe {direction}d text is: {result}\n")

        # Ask to continue
        choice = input("Do you want to process another text? (yes/no): ").strip().lower()
        if choice != "yes":
            print("\nThank you for using the Caesar Cipher App! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
