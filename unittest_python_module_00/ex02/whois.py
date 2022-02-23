def whois(argv):
    
def is_argument_integer(argv):
    try:
        argv[0] = int(argv[0])
        return True
    except ValueError as error:
        return False


def whois(argv):
    try:
        assert is_argument_integer(argv), "argument is not integer"
    except AssertionError as error:
        print(f"{type(error).__name__}: {error}")
    else:
        if (argv[0] == 0):
            print("I'm Zero")
        elif (argv[0] % 2 == 0):
            print("I'm Even")
        else:
            print("I'm Odd")


if __name__ == "__main__":
    try:
        assert len(sys.argv[1:]) > 0, f"Usage: {sys.argv[0]} INTEGER"
        assert len(sys.argv[1:]) < 2, "more than one argument is provided"
    except AssertionError as error:
        print(f"{type(error).__name__}: {error}")
    else:
        whois(sys.argv[1:])

if __name__ == "__main__":
    print(whois(['exec.py', ' ', ' ']))
