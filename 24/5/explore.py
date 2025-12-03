#!/usr/bin/python3
import sys
rules = set()
updates = []
for line_raw in open("input.in"):
	line = line_raw.strip()
	if "|" in line:
		a, _sep, b = line.partition("|")
		rules.add((int(a), int(b)))
	elif "," in line:
		updates.append([int(n) for n in line.split(",")])

rule_numbers = set(n for rule in rules for n in rule)
print(len(rules), len(rule_numbers))
update_numbers = set(n for update in updates for n in update)
print(len(updates), len(update_numbers))
rules_left = {}
# rules_right = {}
for (a, b) in rules:
	rules_left.setdefault(a, set()).add(b)

def find_transitive(num):
	print(num)
	return set(t for n in rules_left.get(num) for t in find_transitive(n))
# rules_transitive = {num: find_transitive(num) for num in rules_left}

print("check missing")
for update in updates:
	for i, page in enumerate(update):
		for page2 in update[i+1:]:
			if not (page, page2) in rules and not (page2, page) in rules:
				print(page, page2)
print("done")
