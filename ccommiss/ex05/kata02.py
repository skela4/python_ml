from datetime import datetime


if __name__ == "__main__":
    t = (3, 0, 19, 9, 25, 78, 789)
    hour, minutes, year, month, day = t
    try:
        print(
            datetime(
                year, month, day, hour, minutes).strftime("%m/%d/%Y %H:%M"))
    except TypeError as msg:
        print(msg)
    except Exception as msg:
        print(msg)
