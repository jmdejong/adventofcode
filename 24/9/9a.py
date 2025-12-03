#!/usr/bin/python3
import sys




FREE = "."

inp = open("input.in").read().strip()

blocks = []
is_file = True
next_id = 0
for c in inp:
	size = int(c)
	if is_file:
		for i in range(size):
			blocks.append(next_id)
		next_id += 1
	else:
		for i in range(size):
			blocks.append(FREE)
	is_file = not is_file

print("".join(str(b) for b in blocks))

def format_disk(blocks):
	to_put = 0
	while True:
		block = blocks.pop()
		if block == FREE:
			continue
		else:
			while to_put < len(blocks) and blocks[to_put] != FREE:
				to_put += 1
			if to_put >= len(blocks):
				blocks.append(block)
				return blocks
			blocks[to_put] = block
			to_put += 1

format_disk(blocks)
print("".join(str(b) for b in blocks))

cs = sum(i * n for i, n in enumerate(blocks))
print(cs)
