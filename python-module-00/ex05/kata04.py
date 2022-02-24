if __name__ == "__main__":
    t = (0, 4, 132.42222, 10000, 12345.67)
    try:
        print("module_{:02d}, ex_{:02d}, {:.2f}, {:.2e}, {:.2e}".format(*t))
    except Exception as msg:
        print(msg)
