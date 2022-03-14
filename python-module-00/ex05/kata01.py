kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumot',
    'PHP': 'Rsmus Lerdorf',
}


def build_iterable(iterable):
    try:
        assert isinstance(iterable, dict), "input is not of type dictionary"
        assert len(iterable) is not 0, "kata is empty"
        for k, v in iterable.items():
            assert isinstance(k, str), "key in dict can only be a string"
            assert isinstance(v, str), "value in dict can only be a string"
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")
    else:
        {print(f"{k} was created by {v}") for k, v in iterable.items()}

if __name__ == "__main__":
    build_iterable(kata)
