#!/usr/bin/python3
import sys

w = -1
h = 0

frequencies = {}


for y, line_raw in enumerate(open("input.in")):
	line = line_raw.strip()
	if line == "":
		break
	h += 1
	w = len(line)
	for x, char in enumerate(line):
		if char.isalnum():
			frequencies.setdefault(char, []).append((x, y))
print(w, h)

res = 0

antennas = {}
antinodes = set()
for char, positions in frequencies.items():
	for first in positions:
		antennas[first] = char
		for second in positions:
			if first == second:
				continue
			dif = (second[0] - first[0], second[1] - first[1])
			p = second
			while True:
				# anti = (p[0] + dif[0], p[1] + dif[1])
				# print(anti)
				if p[0] < 0 or p[0] >= w or p[1] < 0 or p[1] >= h:
					break
				antinodes.add(p)
				p = (p[0] + dif[0], p[1] + dif[1])
	# print(char, antinodes, positions)
for y in range(h):
	for x in range(w):
		pos = (x, y)
		if pos in antinodes:
			sys.stdout.write("#")
		elif pos in antennas:
			sys.stdout.write(antennas[pos])
		else:
			sys.stdout.write(".")
	sys.stdout.write("\n")
	sys.stdout.flush()
print(len(antinodes))
