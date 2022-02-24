if __name__ == "__main__":
    phrase = "format"
    try:
        print(phrase.rjust(42, "-"), end='')
    except Exception as msg:
        print(msg)
