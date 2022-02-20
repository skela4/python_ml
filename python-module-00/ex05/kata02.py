from datetime import datetime


if __name__ == "__main__":
    t = (3, 30, 2019, 9, 25)
    hour, minutes, year, month, day = t
    try:
        print(
            datetime(
                year, month, day, hour, minutes).strftime("%m/%d/%Y %H:%M"))
    except TypeError as msg:
        print(msg)
    except Exception as msg:
        print(msg)
