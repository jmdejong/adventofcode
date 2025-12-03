#!/usr/bin/python3
import sys

FREE = "."

class Vile():
	def __init__(self, id, size, pos):
		self.id = id
		self.size = size
		self.pos = pos
	def checksum(self):
		if self.id == FREE:
			return 0
		return self.id * self.size*(2*self.pos + self.size - 1) // 2
		# return sum(i*self.id for i in range(self.pos, self.pos + self.size))

	def __repr__(self):
		# return f"{self.id}:{self.size}"
		return f"({self.id}: {self.pos}..{self.pos + self.size} |{self.size}|)"

inp = open(sys.argv[1]).read().strip()

holes = []
viles = []
is_file = True
next_id = 0
pos = 0
for c in inp:
	size = int(c)
	if is_file:
		vile = Vile(next_id, size, pos)
		viles.append(vile)
		next_id += 1
	else:
		hole = Vile(FREE, size, pos)
		holes.append(hole)
	pos += size
	is_file = not is_file

for vile in reversed(viles):
	for i, hole in enumerate(holes):
		if hole.pos > vile.pos:
			break
		if hole.size >= vile.size:
			vile.pos = hole.pos
			if hole.size == vile.size:
				holes.pop(i)
			else:
				hole.pos += vile.size
				hole.size -= vile.size
			break

viles.sort(key=lambda vile: vile.pos)

print(sum(vile.checksum() for vile in viles))
fs = []
space = 0
for vile in sorted(viles, key=lambda vile: vile.pos):
	while len(fs) < vile.pos:
		fs.append(".")
		space += 1
	while len(fs) < vile.pos + vile.size:
		fs.append(chr(vile.id + ord('0')))
print("space", space)
print("".join(fs))
