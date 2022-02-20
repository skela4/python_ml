import string
import sys
import string

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/',
}


def encode_morse(args):
    morse_string = []
    for arg in args:
        for char in arg:
            try:
                assert char not in string.punctuation, "ERROR"
            except AssertionError as message:
                raise SystemExit(message)
            char = char.upper()
            if char in morse:
                morse_string.append(morse[char])
    if len(morse_string) > 0:
        print(' '.join(morse_string))

import sys
encode_morse(sys.argv[-1])