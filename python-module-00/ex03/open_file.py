import sys

with open(sys.argv[-1]) as fd:
    text = fd.read()
text_analyzer(text)