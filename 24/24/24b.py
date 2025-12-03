#!/usr/bin/python3
import sys
from functools import cache



fns = {
	"&": (lambda a, b: a & b),
	"|": (lambda a, b: a | b),
	"^": (lambda a, b: a ^ b),
}

opnames = {
	"AND": "&",
	"OR": "|",
	"XOR": "^"
}

initials = {}
gates = []
wires = {}
for line in open(sys.argv[1]):
	if ":" in line:
		wire, _, v = line.strip().partition(": ")
		initials[wire] = int(v)
	elif "->" in line:
		[a, ops, b, _, out] = line.strip().split(" ")
		op = opnames[ops]
		wires[out] = (a, op, b)
		gates.append((a, b, op, out))

LITERAL = "literal"

def evaluate(wire, inp):
	if wire in inp:
		return inp[wire]
	a, op, b = wires[wire]
	return fns[op](evaluate(a, inp), evaluate(b, inp))

bits = "".join(str(evaluate(wire, initials)) for wire in sorted(wires.keys(), reverse=True) if wire[0] == 'z')
print(bits)
print(int(bits, base=2))


for z in sorted(wire for wire in wires if wire[0] == 'z'):
	zid = int(wire[1:])
	for x in [0, 1]:
		for y in [0, 1]:
			for carry in [0, 1]:
				inp = {}
				if x:
					inp[f"x{zid}"] = 1
				if y:
					inp[f"y{zid}"] = 1
				if carry:
					pass
	is_correct = evaluate(z,
	print(f"{z}: {evaluate(z, initials)}")
