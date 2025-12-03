#!/usr/bin/python3
import sys

result = 0
for line in open(sys.argv[1]):
	line = line.strip()
	battery = ""
	c = 12
	while c > 0:
		m = max(line[:-(c-1)] if c > 1 else line)
		i = line.index(m)
		line = line[i+1:]
		battery += m
		c -= 1
	v = int(battery)
	print(" ", v)
	result += v
print(result)
