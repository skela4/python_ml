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
    """This function counts the number of upper characters,\n\
lower characters, punctuation and spaces in a given text"""

    try:
        if (len(sys.argv[0]) > 0):
            assert len(arg) == 0, f"Usage: {sys.argv[0]} STRING"
        else:
            assert len(arg) == 0, f"Usage: text_analyzer(STRING)"
    except AssertionError as error:
        print(error)
        return None

    if (not isinstance(text, str) and text is not None):
        print("argument is not a string")
        return None

    if text is not None or len(text) == 0:
        text = input('What is the text to analyse?\n')

    dict_char = count(text)
    print(f"The text contains {dict_char['total']} characters")
    print(f"- {dict_char['upper']} upper letter")
    print(f"- {dict_char['lower']} lowers letters")
    print(f"- {dict_char['punc']} punctuation marks")
    print(f"- {dict_char['space']} spaces")
    return None


if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        text_analyzer("")
    else:
        text_analyzer(sys.argv[1], *sys.argv[2:])
