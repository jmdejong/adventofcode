#!/usr/bin/env python3

import sys

total = 0
for line in sys.stdin:
	module = 0
	ff = int(line) // 3 - 2
	while ff >= 0:
		module += ff
		ff = ff // 3 - 2
	total += module

print(total)
