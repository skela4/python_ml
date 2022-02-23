# TODO change exec function for a program

import string


def join_rev_strings(strings):
    result = []
    delimiters = "|".join(string.whitespace)
    for s in strings:
        s = s.strip(string.whitespace).swapcase()
        if len(s) > 0:
            result.append(s)
    print('[DEBUG] ==> result: ', result, end='\n')
    return " ".join(result)[::-1]


def exec(argv):
    if len(argv) == 1:
        return f"Usage: {argv[0]} STRING..."
    elif len(argv) == 2:
        return argv[1].strip(string.whitespace).swapcase()[::-1]
    else:
        return join_rev_strings(argv[1:])


if __name__ == "__main__":
    print(exec(['exec.py', ' ', ' ']))