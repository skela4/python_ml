from datetime import datetime

kata = (2019, 9, 25, 3, 30)


def check_iterable(kata):
    assert isinstance(kata, tuple), (
        "input is not of type tuple"
    )
    assert all([isinstance(e, int) for e in kata]), (
        "value in tuple can only be a integer"
    )


if __name__ == "__main__":
    try:
        year, month, day, hour, minutes = kata
        check_iterable(kata)
        d = datetime(year, month, day, hour, minutes)
        print(d.strftime('%m/%d/%Y %H/%M'))
    except (AssertionError, ValueError) as error:
        raise SystemExit(f"{type(error).__name__}: {error}")
