kata = (0, 4, 132.4222, 10000, 12345.67)

if __name__ == "__main__":
    try:
        assert isinstance(kata, tuple), "kata need to be a tuple"

        module, ex, decimal, integer, second_decimal = kata

        assert module >= 0 and module < 100 and ex >= 0 and ex < 100, (
            "first and third params need to be non-negative integer up to 2 digits"
        )
        assert isinstance(ex, float) and isinstance(integer, float), (
            "second and fourth params need to be non-negative"
        )
        assert isinstance(decimal, int) and isinstance(second_decimal, int), (
            "first and second params need to be non-negative"
        )

        print("module_{:02d}, ex_{:02d}, {:.2f}, {:.2e}, {:.2e}".format(*t))
    except Exception as error:
        raise SystemExit(f"{type(error).__name__}: {error}")

# titre ynov