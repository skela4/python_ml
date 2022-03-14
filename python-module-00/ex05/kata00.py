t = (19,)


def build_iterable(iterable):
    result = []
    try:
        assert isinstance(iterable, tuple), "input is not of type tuple"
        assert len(iterable) is not 0, "kata is empty"
        for elem in iterable:
            try:
                assert isinstance(elem, int), "can only be filled with integer"
            except AssertionError as error:
                raise SystemExit(f"{AssertionError.__name__}: {error}")
            else:
                result.append(elem)
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")
    typo = 'numbers are' if len(result) > 1 else 'number is'
    print(f"the {len(result)} {typo}: {', '.join(map(str, result))}")


if __name__ == "__main__":
    build_iterable(t)
