import sys


def exec(argv):
    if len(argv) == 1:
        return f"Usage: {argv[0]} STRING..."
    elif len(argv) == 2:
        return argv[1].swapcase()[::-1]
    else:
        return ' '.join([s.swapcase() for s in argv[1:] if len(s) > 0])[::-1]


if __name__ == '__main__':
    print(exec(sys.argv))
