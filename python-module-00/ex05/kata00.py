t = (19, 42, 21)

def build_iterable(iterable):
    result = []
    try:
        assert len(iterable) is not 0, "kata is empty"
        assert isinstance(iterable, tuple), "input is not of type tuple"
        for integer in iterable:
            try:
                assert isinstance(integer, int), "tuple can only be filled with integer"
            except AssertionError as error:
                raise SystemExit(f"{AssertionError.__name__}: {error}")
            else:
                result.append(integer)
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")
    if (len(result) is 1):
        print(f"the {len(result)} number is: {', '.join(map(str, result))}")
    else:
        print(f"the {len(result)} numbers are: {', '.join(map(str, result))}")

if __name__ == "__main__":
    build_iterable(t)
