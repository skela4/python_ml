import sys


if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} STRING...")
    result = []
    for str_arg in sys.argv[1:]:
        if len(str_arg) > 0:
            result.append(str_arg.swapcase())
    print(" ".join(result)[::-1])
