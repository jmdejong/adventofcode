#!/usr/bin/python3
import sys
from itertools import *


def flip(strings):
	return ["".join(column) for column in zip_longest(*strings, fillvalue=" ")]

def skew(strings):
	return [" "*i + string for i, string in enumerate(strings)]


inp = [line.strip() for line in sys.stdin if len(line.strip())]

transforms = [
	*inp,
	*flip(inp),
	*[s.strip() for s in flip(skew(inp))],
	*[s.strip() for s in flip(skew(reversed(inp)))],
]
transforms += ["".join(reversed(line)) for line in transforms]
print(sum(line.count("XMAS") for line in transforms))
