def join_rev_strings(strings):
    return " ".join([s.swapcase() for s in strings if len(s) > 0])[::-1]

def exec(argv):
    if len(argv) == 1:
        return f"Usage: {argv[0]} STRING..."
    elif len(argv) == 2:
        return argv[1].swapcase()[::-1]
    else:
        return join_rev_strings(argv[1:])
