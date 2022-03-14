import sys
import string


def count(text):
    dict_char = {
        'lower': 0,
        'upper': 0,
        'punc': 0,
        'space': 0,
        'total': 0,
    }

    for char in text:
        dict_char['total'] += 1
        if char.islower():
            dict_char['lower'] += 1
        elif char.isupper():
            dict_char['upper'] += 1
        elif char in string.punctuation:
            dict_char['punc'] += 1
        elif char in string.whitespace:
            dict_char['space'] += 1
    return dict_char


def text_analyzer(text="", *arg):
    """
    This function counts the number of upper characters, lower characters,\n\
    punctuation and spaces in a given text
    """

    try:
        assert len(arg) == 0, f"Usage: text_analyzer(STRING)"
        assert text is None or isinstance(text, str), f"argument is not a string"
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None

    while len(text) == 0:
        text = input('What is the text to analyse?\n')

    dict_char = count(text)
    print(f"The text contains {dict_char['total']} character(s)")
    print(f"- {dict_char['upper']} upper letter(s)")
    print(f"- {dict_char['lower']} lower letter(s)")
    print(f"- {dict_char['punc']} punctuation mark(s)")
    print(f"- {dict_char['space']} space(s)")
    return None


if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        text_analyzer("")
    else:
        text_analyzer(sys.argv[1], *sys.argv[2:])

# "Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles."
# "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace."
# "Hello World!"
