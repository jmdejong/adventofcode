#!/usr/bin/python3
import sys

result = 0
for line in open(sys.argv[1]):
	line = line.strip()
	m = '0'
	m2 = '0'
	for c in line[:-1]:
		if c > m:
			m = c
			m2 = '0'
		elif c > m2:
			m2 = c
	if line[-1] > m2:
		m2 = line[-1]
	v = int(m + m2)
	print(" ",v)
	result += v
print(result)

