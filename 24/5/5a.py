#!/usr/bin/python3
import sys

forbidden_after = {}
count = 0
for line_raw in sys.stdin:
	line = line_raw.strip()
	if "|" in line:
		a, _sep, b = line.partition("|")
		forbidden_after.setdefault(b, []).append(a)
	if "," in line:
		items = line.split(",")
		banned = {}
		valid = True
		for item in items:
			if item in banned:
				valid = False
				break
			for forbidden in forbidden_after.get(item, []):
				banned[forbidden] = item
		if valid:
			n = int(items[len(items)//2])
			# print(n," ", line)
			count += n
# print(forbidden_after)
print(count)
