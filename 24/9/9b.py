#!/usr/bin/python3
import sys

FREE = "."

class Vile():
	def __init__(self, id, size):
		self.id = id
		# self.pos = pos
		self.size = size
	def __repr__(self):
		return f"{self.id}:{self.size}"
		# return f"({self.id}: {self.pos}..{self.pos + self.size} |{self.size}|)"



inp = open(sys.argv[1]).read().strip()

viles = []
is_file = True
next_id = 0
# pos = 0
for c in inp:
	size = int(c)
	if is_file:
		vile = Vile(next_id, size)
		next_id += 1
	else:
		vile = Vile(FREE, size)
	viles.append(vile)
	# pos += size
	is_file = not is_file

print("".join(str(vile.id) * vile.size for vile in viles))
last_id = infinity
while True:
	to_move = viles.pop()
	if to_move.id == FREE:
		viles.push(to_move)
	for i, vile in enumerate(viles):
		if vile.id == FREE and vile.size >= to_move.size:
			vile.size -= to_move.size
			if vile.size == 0:
				viles[i] = to_move
			else:
				viles.insert(i, to_move)
			break
		else:
			viles.push(to_move)
print("".join(str(vile.id) * vile.size for vile in viles))

# cs = sum(i * n for i, n in enumerate(blocks))
# print(cs)
