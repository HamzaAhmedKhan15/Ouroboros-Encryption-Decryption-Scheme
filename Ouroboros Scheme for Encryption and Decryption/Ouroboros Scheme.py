# -*- coding: utf-8 -*-
"""NIS Project.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I45JewGcfkV7VV08O2wdFI0PJXl0bt3s

#CT-20035- Hamza Ahmed Khan
#NIS COURSE PROJECT

To Encrypt, Run the code and press 1.

After the encryption copy the encrypted text and run code again and press 2 for Decryption.
"""

################################################### ENCRYPTION ##################################################

def reverse_text(text):
    reversed_text = text[::-1]
    return reversed_text


def print_ascii_code(text, block_size, alphabet_mapping):
    original_ascii_codes = []
    new_ascii_codes = []

    for character in text:
        ascii_code = ord(character)
        new_ascii_code = ascii_code + block_size

        original_ascii_codes.append(f"{character}: {ascii_code}")
        new_ascii_codes.append(
            f"{character}: {ascii_code} + {block_size} = {new_ascii_code}"
        )

    print("\nOriginal ASCII Codes:", ", ".join(original_ascii_codes))
    print("\nNew ASCII Codes:", ", ".join(new_ascii_codes))

    print("\nAlphabet Mapping:")
    for new_ascii_code, character in alphabet_mapping.items():
        print(f"{new_ascii_code} = {character}")

    # Print the alphabet characters in a row
    print("\nEncrypted Text:", "".join(alphabet_mapping.values()))
    print("\n")


################################################### DECRYPTION ##################################################


def reverse_and_transform(input_str):
    # Reverse the string
    reversed_str = input_str[::-1]
    print("\nReversed String:", reversed_str)

    # ASCII codes of the reversed string
    reversed_ascii_codes = {char: ord(char) for char in reversed_str}
    original_ascii_codes = [
        f"{char}: {ascii_code}" for char, ascii_code in reversed_ascii_codes.items()
    ]
    print("\nOriginal ASCII Codes:", ", ".join(original_ascii_codes))

    # Subtract 2 from each ASCII code during decryption
    block_size = 2
    transformed_ascii_codes = {
        char: code - block_size for char, code in reversed_ascii_codes.items()
    }
    new_ascii_codes = [
        f"{char}: {code} - {block_size} = {code - block_size}"
        for char, code in transformed_ascii_codes.items()
    ]
    print("\nNew ASCII Codes:", ", ".join(new_ascii_codes))

    # Alphabets mapping of the subtracted ASCII codes
    print("\nAlphabet Mapping:")
    for code, char in transformed_ascii_codes.items():
        print(f"{code} = {char}")

    # Print the alphabet characters in a row
    mapped_chars = "".join([chr(code) for code in transformed_ascii_codes.values()])
    print("\nDecrypted Text:", mapped_chars)
    print("\n")


# Prompt user to choose encryption or decryption
choice = input(
    "\nMy  Encryption / Decryption  Scheme: \n1. Encryption \n2. Decryption: \n"
)

if choice == "1":
    # Encryption
    plaintext = input("\nEnter the text you want to Encrypt: ")
    block_size = int(input("\nEnter Secret Key: "))  # Convert block_size to integer
    alphabet_mapping = {}  # Create a new alphabet mapping

    reversed_plaintext = reverse_text(plaintext)

    for character in reversed_plaintext:
        ascii_code = ord(character)
        new_ascii_code = ascii_code + block_size

        # Handle repeating letters by appending an index
        i = 0
        while new_ascii_code in alphabet_mapping:
            i += 1
            new_ascii_code = ascii_code + block_size + i

        alphabet_mapping[new_ascii_code] = chr(
            new_ascii_code
        )  # Add mapping to the dictionary

    print("\nReversed Text:", reversed_plaintext)
    print_ascii_code(reversed_plaintext, block_size, alphabet_mapping)

elif choice == "2":
    # Decryption
    user_input = input("\nEnter the text you want to Decrypt: ")
    reverse_and_transform(user_input)

else:
    print("Invalid choice. Please enter '1' for Encrypt or '2' for Decrypt.")