#!/usr/bin/python3
import sys
import functools
rules = set()
updates = []
for line_raw in open("input.in"):
	line = line_raw.strip()
	if "|" in line:
		a, _sep, b = line.partition("|")
		rules.add((int(a), int(b)))
	elif "," in line:
		updates.append([int(n) for n in line.split(",")])


rules_left = {}
rules_right = {}
for (a, b) in rules:
	rules_left.setdefault(a, set()).add(b)
	rules_right.setdefault(b, set()).add(a)

def comp_page(a, b):
	if (a, b) in rules:
		return 1
	elif (b, a) in rules:
		return -1
	else:
		print("unknown order", a, b)

def mid(arr):
	return arr[len(arr)//2]

valid_count = 0
fixed_count = 0
for update in updates:
	banned = {}
	valid = True
	for page in update:
		if page in banned:
			valid = False
			break
		for forbidden in rules_right.get(page, []):
			banned[forbidden] = page
	if valid:
		valid_count += mid(update)
	else:
		sorted_update = sorted(update, key=functools.cmp_to_key(comp_page))
		# print(update)
		# print(sorted_update)
		fixed_count += mid(sorted_update)
print(valid_count)
print(fixed_count)


