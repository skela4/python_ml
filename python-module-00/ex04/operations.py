import sys


def usage():
    error = f"Usage: {sys.argv[0]} <number1> <number2>\n"
    error += "Example:\n"
    error += "   python operations.py 10 3"
    return error


def check_args(args):
    try:
        assert len(args) > 1, usage()
    except AssertionError as msg:
        raise SystemExit(msg)

    try:
        assert len(args) == 2, "InputError: too many arguments\n"
    except AssertionError as msg:
        print(msg)
        raise SystemExit(usage())

    try:
        return (int(args[0]), int(args[1]))
    except ValueError as msg:
        print("InputError: only numbers\n")
        raise SystemExit(usage())


def print_pad(operation_string, result):
    print(operation_string.ljust(11, " "), result)


def operation(a, b):
    print_pad("Sum:", a + b)
    print_pad("Difference:", a - b)
    print_pad("Product:", a * b)
    if (b == 0):
        print_pad("Quotient", "ERROR (div by zero)")
        print_pad("Remainder", "ERROR (modulo by zero)")
    else:
        print_pad("Quotient", a / b)
        print_pad("Remainder", a % b)


if __name__ == "__main__":
    args = sys.argv[1:]
    num1, num2 = check_args(args)
    operation(num1, num2)
