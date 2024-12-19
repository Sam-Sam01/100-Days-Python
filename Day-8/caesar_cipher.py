import string

# def encrypt(plain_text, shift_number):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = (position + shift_number) % 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_number):
#     decrypt_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = (position - shift_number) % 26
#         new_letter = alphabet[new_position]
#         decrypt_text += new_letter
#     print(f"the decrypted text is {decrypt_text}")


def cipher(plain_text, direction, shift_number):
    def encrypt(p_text, s_number):
        ceaser_text = ""
        for letter in p_text:
            position = alphabet.index(letter)
            new_position = (position + s_number)%26
            new_letter = alphabet[new_position]
            ceaser_text += new_letter
        return ceaser_text
    
    if direction == "encode":
        return encrypt(plain_text, shift_number)
    else:
        return encrypt(plain_text, -shift_number)

alphabet = list(string.ascii_lowercase)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message:").lower()
shift = int(input("Type your shift number:\n"))

r_text = cipher(plain_text=text, direction=direction, shift_number=shift)
print("%s"%r_text)
# if direction == "encode":
#     encrypt(plain_text=text, shift_number=shift) 
# else:
#     decrypt(cipher_text=text, shift_number=shift)


