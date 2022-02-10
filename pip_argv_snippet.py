# pip_argv_snippet.py
import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]
