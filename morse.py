import winsound
import time

# The magical dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# I DON'T THINK COMENT IS NECESARRY
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morse_to_text(morse):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(code, '') for code in morse.split())

def play_morse_audio(morse):
    for symbol in morse:
        if symbol == '.':
            winsound.Beep(1000, 200)  # Dot: 200ms beep
        elif symbol == '-':
            winsound.Beep(1000, 600)  # Dash: 600ms beep
        elif symbol == ' ':
            time.sleep(0.6)  # Space between letters
        time.sleep(0.2)  # Space between symbols

def main():
    while True:
        choice = input("Choose an option: (1) Text to Morse, (2) Morse to Text, (Q) Quit: ").strip().upper()
        
        if choice == '1':
            text = input("Enter text to convert to Morse Code: ")
            morse = text_to_morse(text)
            print("Morse Code:", morse)
            play_morse_audio(morse)
        elif choice == '2':
            morse = input("Enter Morse Code to convert to text (use space between letters): ")
            text = morse_to_text(morse)
            print("Text:", text)
        elif choice == 'Q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
