import sys
import re

if __name__ == "__main__":
    args = sys.argv[1:]

    try:
        assert len(args) == 2
        str = args[0]
        n = int(args[1])
    except Exception:
        raise SystemExit("Error")

    results = re.split(r'\W+', str)
    # print (results)
    results = [result for result in results if len(result) > n]
    print(results)
