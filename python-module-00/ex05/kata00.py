def build_iterable(iterable):
    print(f"the {len(iterable)} numbers are: {', '.join(map(str, iterable))}")


if __name__ == "__main__":
    t = (19, 42, 'Salut', 42)
    try:
        [int(integer) for integer in t]
    except Exception as msg:
        raise SystemExit("InputError: only numbers\n")
    else:
        build_iterable(t)
