#!/usr/bin/python3
import sys



def evolve(num, times=1):
	for i in range(times):
		num = (num ^ (num * 64)) % 16777216
		num = (num ^ (num // 32)) % 16777216
		num = (num ^ (num * 2048)) % 16777216
	return num

initials = [int(line.strip()) for line in open(sys.argv[1])]
# print(len(initials))
# for num in initials:
	# print(num, evolve(num, 2000))
print(sum(evolve(num, 2000) for num in initials))
