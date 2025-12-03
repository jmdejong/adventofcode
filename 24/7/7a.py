#!/usr/bin/python3


def can_make(total, parts, curr=0):
	if len(parts) == 0:
		return total == curr
	else:
		return can_make(total, parts[1:], curr+parts[0]) or can_make(total, parts[1:], curr*parts[0])


res = 0

for line_raw in open("input.in"):
	line = line_raw.strip()
	if line == "":
		break
	head, _sep, rest = line.partition(": ")
	total = int(head)
	parts = [int(val) for val in rest.split()]
	if can_make(total, parts):
		res += total
		print(line)
print(res)
