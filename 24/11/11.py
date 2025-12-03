#!/usr/bin/python3
import sys

cache = {}

def nr_expansions(num, blinks):
	key = (num, blinks)
	if key not in cache:
		cache[key] = count_expansions(num, blinks)
	return cache[key]

def count_expansions(num, blinks):
	if blinks == 0:
		return 1
	if num == 0:
		return nr_expansions(1, blinks-1)
	s = str(num)
	if len(s) % 2 == 0:
		return nr_expansions(int(s[:len(s)//2]), blinks-1) + nr_expansions(int(s[len(s)//2:]), blinks-1)
	return nr_expansions(num*2024, blinks-1)

stones = [int(s) for s in open(sys.argv[1]).read().strip().split()]
print(stones)
print(sum(nr_expansions(stone, 25) for stone in stones))
print(sum(nr_expansions(stone, 75) for stone in stones))
print(sum(nr_expansions(stone, 100) for stone in stones))
print(sum(nr_expansions(stone, 200) for stone in stones))
print(sum(nr_expansions(stone, 500) for stone in stones))
# print(sum(nr_expansions(stone, 1000) for stone in stones))

