# whois.py.py
import sys


def test_assertion(args):
    try:
        num = args[0]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} INTEGER")

    assert len(args) == 1, "more than one argument is provided"
    assert (num.isdigit()), "argument is not integer"
    return int(num, 10)


def whois(num):
    print(num)
    if (num == 0):
        print("I'm Zero")
    elif (num % 2 == 0):
        print("I'm Even")
    else:
        print("I'm Odd")


if __name__ == "__main__":
    try:
        args = sys.argv[1:]
        num = test_assertion(args)
    except AssertionError as error:
        assertion_type = type(error).__name__
        print(f"{assertion_type}: {error}")
    else:
        whois(num)
