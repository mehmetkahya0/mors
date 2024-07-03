# python morse.py -i "input.txt" -o "output.txt" -m "encode"

import argparse
import sys
import os
import re
from colorama import Fore, Style
import time

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse Morse code dictionary

reverse_morse_code = {value: key for key, value in morse_code.items()}

def encode(text):
    encoded_text = ''
    for char in text:
        if char.upper() in morse_code:
            encoded_text += morse_code[char.upper()] + ' '
        else:
            encoded_text += char
    return encoded_text

def decode(text):
    decoded_text = ''
    for char in text.split(' '):
        if char in reverse_morse_code:
            decoded_text += reverse_morse_code[char]
        else:
            decoded_text += char
    return decoded_text

def main():
    # Using method: python3 main.py -i 'STRING' -o 'output.txt' -m 'encode'
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input text")
    parser.add_argument("-o", "--output", help="Output text")
    parser.add_argument("-m", "--method", help="Method: encode or decode")
    args = parser.parse_args()

    if args.method == 'encode':
        print(Fore.GREEN + "Encoding..." + Style.RESET_ALL)
        time.sleep(1)
        encoded_text = encode(args.input)
        print(Fore.GREEN + "Encoded text: " + Style.RESET_ALL + encoded_text)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(encoded_text)
                print(Fore.GREEN + "Encoded text saved to " + args.output + Style.RESET_ALL)

    elif args.method == 'decode':
        print(Fore.GREEN + "Decoding..." + Style.RESET_ALL)
        time.sleep(1)
        decoded_text = decode(args.input)
        print(Fore.GREEN + "Decoded text: " + Style.RESET_ALL + decoded_text)
        if args.output:
            with open(args.output, 'w') as f:
                f.write(decoded_text)
                print(Fore.GREEN + "Decoded text saved to " + args.output + Style.RESET_ALL)

    else:
        print(Fore.RED + "Invalid method. Please use encode or decode" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()

