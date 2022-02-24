def build_iterable(iterable):
    result = []
    try:
        assert isinstance(iterable, tuple), "input is not of type tuple"
        assert len(iterable) > 0, "tuple is empty"
        for integer in iterable:
            try:
                integer = int(integer)
            except Exception:
                pass
            else:
                result.append(integer)
    except Exception as msg:
        raise SystemExit(msg)
    if len(result) > 0:
        print(
            f"the {len(result)} numbers are: {', '.join(map(str, result))}"
        )
    else:
        print('tuple does not contain number')


if __name__ == "__main__":
    t = ("19", "42", "21", "78", "8674")
    build_iterable(t)
