import string

dict_char = {
    'lower': 0,
    'upper': 0,
    'punc': 0,
    'space': 0,
    'total': 0,
}


def count(char):
    dict_char['total'] += 1
    if char.islower():
        dict_char['lower'] += 1
    elif char.isupper():
        dict_char['upper'] += 1
    elif char in string.punctuation:
        dict_char['punc'] += 1
    elif char in string.whitespace:
        dict_char['space'] += 1


def text_analyzer(text="", *arg):
    """This function counts the number of upper characters,\n\
lower characters, punctuation and spaces in a given text"""

    if len(arg) > 0:
        raise SystemExit("ERROR")

    if len(text) == 0:
        while len(text) == 0:
            text = input('What is the text to analyse?\n')

    list(map(count, text))
    print(f"The text contains {dict_char['total']} characters")
    print(f"- {dict_char['upper']} upper letter")
    print(f"- {dict_char['lower']} lowers letters")
    print(f"- {dict_char['punc']} punctuation marks")
    print(f"- {dict_char['space']} spaces")
