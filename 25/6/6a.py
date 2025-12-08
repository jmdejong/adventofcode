#!/usr/bin/python3
import sys
from functools import *
import operator
rows = [line.strip().split() for line in open(sys.argv[1])]
columns = list(zip(*[[int(n) for n in c] for c in rows[:-1]]))
operators = rows[-1]
# print(columns)
answers = [sum(col) if op == "+" else reduce(operator.mul, col, 1) for col, op in zip(columns, operators)]
print(answers)
total = sum(answers)
print(total)
