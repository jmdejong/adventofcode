#!/usr/bin/python3
import sys

reports = [[int(word) for word in line.split()] for line in sys.stdin if len(line.strip())]
# print(reports)
# print(min(len(report) for report in reports))

def simple_safe(report):
	is_increasing = report[1] > report[0]
	previous = report[0]
	for level in report[1:]:
		diff = abs(level-previous)
		if (level > previous) != is_increasing:
			# print("dir", level, previous, report)
			return False
		if diff > 3:
			# print("step", level, previous, report)
			return False
		if diff < 1:
			# print("same", level, previous, report)
			return False
		previous = level
	return True


def try_safe(report):
	for i in range(len(report)):
		c = report.copy()
		del c[i]
		if simple_safe(c):
			return True
	return False


def is_safe(report, allow_skip):
	directions = [0, 0]
	previous = report[0]
	for level in report[1:]:
		directions[int(level > previous)] += 1
		previous = level
	# print(directions)
	if min(directions) > int(allow_skip):
		print("unsafe directions", report)
		return False
	is_increasing = directions[1] > directions[0]
	previous = report[0]
	skipped = None
	for level in report[1:]:
		bad = None
		if (level > previous) != is_increasing:
			bad = "dir"
		elif abs(level - previous) > 3:
			bad = "step"
		elif level == previous:
			bad = "same"

		if bad != None:
			res = (bad, previous, level)
			# print("bad", previous, level)
			if skipped == None and allow_skip:
				skipped = res
			else:
				print("unsafe", report)
				print(skipped)
				print(res)
				return False
		else:
			previous = level
	# print("safe")
	return True


safe = 0
for report in reports:
	safe += int(try_safe(report))
	# safe += int(is_safe(report, True) or is_safe(report[1:], False))
print(safe)
