if __name__ == "__main__":
    phrase = "The right format%"
    try:
        print(phrase.rjust(41, "-"))
    except Exception as msg:
        print(msg)
