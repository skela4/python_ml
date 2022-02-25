import sys

def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def whois(argv):
    try:
        assert 0 < len(argv[1:]) , f"Usage: {argv[0]} INTEGER"
        assert len(argv[1:]) < 2, "AssertionError: more than one argument is provided"
        assert is_integer(argv[1]), "AssertionError: argument is not integer"
    except AssertionError as error:
        return f"{error}"
    else:
        if (int(argv[1]) == 0):
            return "I'm Zero"
        elif (int(argv[1]) % 2 == 0):
            return "I'm Even"
        else:
            return "I'm Odd"


if __name__ == "__main__":
    print(whois(sys.argv))
