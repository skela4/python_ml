kata = (0, 4, 132.4222, 10000, 12345.67)

if __name__ == "__main__":
    try:
        assert isinstance(kata, tuple), "kata need to be a tuple"
        module, ex, decimal, integer, second_decimal = kata
        assert all([isinstance(e, int) for e in [module, ex, integer]]), (
            "first and second and fourth params "
            "need to be integer"
        )
        assert all([e >= 0 and e < 100 for e in [module, ex]]), (
            "first and second params "
            "need to be a non-negative integer up to 2 digits"
        )
        assert all([isinstance(e, float) for e in [decimal, second_decimal]]), (
            "third and fith param "
            "need to be a decimal"
        )
        print("module_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}".format(*kata))
    except Exception as error:
        raise SystemExit(f"{type(error).__name__}: {error}")
