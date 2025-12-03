#!/usr/bin/python3
import sys


fns = {
	"AND": (lambda a, b: a & b),
	"OR": (lambda a, b: a | b),
	"XOR": (lambda a, b: a ^ b),
}

values = {}
gates = []
for line in open(sys.argv[1]):
	if ":" in line:
		wire, _, v = line.strip().partition(": ")
		values[wire] = int(v)
	elif "->" in line:
		[a, op, b, _, out] = line.strip().split(" ")
		gates.append((a, b, op, out))

i = 0
while len(gates):
	i %= len(gates)
	a, b, op, out = gates[i]
	if a in values and b in values:
		values[out] = fns[op](values[a], values[b])
		del gates[i]
	else:
		i += 1

print("\n".join(f"{var}: {val}" for var, val in sorted(values.items())))
bits = "".join(str(val) for var, val in sorted(values.items(), reverse=True) if var[0] == "z")
print(bits)
print(int(bits, base=2))
