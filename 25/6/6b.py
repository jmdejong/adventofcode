#!/usr/bin/python3
import sys
from functools import *
import operator
rows = [line[:-1] for line in open(sys.argv[1])]
# numrows = rows[:-1]
operators = rows[-1][::-1]
# for i in range(
columns = ["".join(line) for line in zip(*rows[:-1])][::-1]
print(rows, columns, operators)
total = 0
a = []
for i, col in enumerate(columns):
	col = col.strip()
	if col == "":
		continue
	a.append(int(col))
	answer = 0
	print(operators[i], a)
	if operators[i] == "+":
		answer = sum(a)
		a = []
	elif operators[i] == "*":
		answer = reduce(operator.mul, a, 1)
		a = []
	print(answer)
	total += answer
print(total)
# print("\n".join(columns[:20]))
