import sys


def exec(argv):
    if len(argv[1:]) == 0:
        return f"Usage: {argv[0]} STRING..."
    else:
        return ' '.join([s.swapcase() for s in argv[1:] if len(s) > 0])[::-1]


if __name__ == '__main__':
    print(exec(sys.argv))
