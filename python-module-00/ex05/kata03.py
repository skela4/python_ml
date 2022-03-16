kata = "The right format"

if __name__ == "__main__":
    try:
        assert isinstance(kata, str), "kata need to be a string"
        assert len(kata) <= 42, "lenght cannot be higher than 42"
        print(kata.rjust(42, "-"), end='')
    except AssertionError as error:
        raise SystemExit(f"{type(error).__name__}: {error}")
    except Exception as error:
        raise SystemExit(f"{type(error).__name__}: {error}")
