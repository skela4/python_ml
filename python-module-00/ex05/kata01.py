def build_iterable(languages):
    for key, value in languages.items():
        print(f"{key} was created by {value}")


if __name__ == "__main__":
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumot',
        'PHP': 'Rsmus Lerdorf',
    }
    try:
        build_iterable(languages)
    except Exception as msg:
        print(msg)
