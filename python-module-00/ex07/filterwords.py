import sys
import re

if __name__ == "__main__":
    args = sys.argv[1:]

    try:
        assert len(args) == 2
        str = args[0]
        n = int(args[1], 10)
    except:
        raise SystemExit("Error")

    results = re.split(r'\W+', str)
    results = [result for result in results if len(result) > n ]
    print(results)