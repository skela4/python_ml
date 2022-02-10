# whois.py.py
import sys


if __name__ == "__main__":
    try:
        args = sys.argv[1:]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} INTEGER")

    # if 