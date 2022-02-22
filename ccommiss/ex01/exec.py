import sys
import re
import string


def rev_str(str: str) -> str:
    return str[::-1]


def strip_str(str: str) -> str:
    return str.strip(string.whitespace)


def not_empty_string(str):
    return len(str) > 0


if __name__ == "__main__":
    try:
        sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} STRING...")

    results = []
    delimiters = "|".join(string.whitespace)

    for arg in sys.argv[1:]:
        strings = list(filter(not_empty_string, re.split(delimiters, arg)))
        for _str in strings:
            results.append(_str)
    print(rev_str(" ".join(strip_str(_str) for _str in results)).swapcase())
