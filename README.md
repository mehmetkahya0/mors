## Morse Code Translator

This Python script provides functionality to encode and decode text using Morse code.

### Functions

#### `encode(text)`
- Takes a string `text` as input.
- Iterates over each character in the input.
- Converts the character to its Morse code representation if it exists in the `morse_code` dictionary.
- Returns the encoded string with Morse code characters separated by spaces.

#### `decode(text)`
- Accepts a string `text` containing Morse code.
- Splits the input string by spaces to process each Morse code character individually.
- Converts each Morse code character back to its alphanumeric representation using the `reverse_morse_code` dictionary.
- Returns the decoded alphanumeric string.

### Main Functionality

- The script starts by displaying an ASCII art logo.
- It then parses command-line arguments for input text, output file, and method (encode or decode).
- If the method is `encode`, it:
  - Prints "Encoding..." to the console.
  - Calls the `encode` function with the input text.
  - Prints the encoded text to the console.

### Usage

To use this script, run the following command in your terminal:

```bash
python3 main.py -i 'Your text here' -o 'output.txt' -m 'encode'
-i or --input: Specifies the input text to be encoded or decoded.
-o or --output: Specifies the file path to save the output text. (This functionality is mentioned in the comments but not implemented in the provided code excerpt.)
-m or --method: Specifies the operation mode, either encode or decode.
```