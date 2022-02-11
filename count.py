import inspect
import string
import sys
import textwrap

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
    """This function counts the number of upper characters, \
    lower characters, punctuation and spaces in a given text.
    """

    if len(arg) > 0:
        raise SystemExit("ERROR")

    if len(text) == 0:
        text = input('What is the text to analyse?\n')
    list(map(count, text))

    print(f"The text contains {dict_char['total']} characters:")
    print(f"- {dict_char['upper']} upper letters")
    print(f"- {dict_char['lower']} lowers letters")
    print(f"- {dict_char['punc']} punctuation marks")
    print(f"- {dict_char['space']} spaces")


if __name__ == "__main__":
    # text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collection reference cycles.")
    # text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
    # print(dir(text_analyzer))

    print(text_analyzer.__doc__)
    text_analyzer("", "vfd")
