# exec.py
import sys


def rev_str(str: str) -> str:
    return str[::-1]


def strip_str(str: str) -> str:
    return str.strip(' \t\n\r\v\f')


if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} STRING...")
    print(rev_str(" ".join(strip_str(arg) for arg in sys.argv[1:])).swapcase())
