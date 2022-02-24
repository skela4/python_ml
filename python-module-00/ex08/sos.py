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


def encode_morse(*args):
    s = " ".join([arg for arg in args if len(arg) > 0])
    morse_string = []
    for char in s:
        char = char.upper()
        try:
            assert char in morse.keys(), "ERROR"
        except AssertionError as message:
            raise SystemExit(message)
        morse_string.append(morse[char])
    if len(morse_string) > 0:
        print(' '.join(morse_string))
