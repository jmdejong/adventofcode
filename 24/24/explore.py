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

@cache
def expression(wire):
	if wire[0] in "xy":
		return (LITERAL, wire)
	a, op, b = wires[wire]
	return (op, [expression(a), expression(b)])


def etos(e):
	op, args = e
	if op == LITERAL:
		return args
	else:
		return f"({f" {op} ".join(etos(arg) for arg in args)})"
	# e = f"{expression(a)} {opnames[op]} {expression(b)}"
	# return e if top else f"({e})"

def simplify(e):
	op, args = e
	if op == LITERAL:
		return e
	newargs = []
	for arg in args:
		subop, subargs = simplify(arg)
		# print(subop)
		if subop == op:
			# print("simplification")
			newargs.extend(subargs)
		else:
			# print(subop, op)
			newargs.append(arg)
	return (op, sorted(newargs))

# prev_e = "@None"
# prev_z = None
for z in sorted(wire for wire in wires if wire[0] == 'z'):
	e = expression(z)
	es = simplify(e)
	# if prev_e in e:
		# e = e.replace(prev_e, prev_z)
	print(f"{z}: {etos(e)}")
	# prev_e = e
	# prev_z = z

# values = initials.copy()
# i = 0
# while len(gates):
# 	i %= len(gates)
# 	a, b, op, out = gates[i]
# 	if a in values and b in values:
# 		values[out] = fns[op](values[a], values[b])
# 		del gates[i]
# 	else:
# 		i += 1
#
# print("\n".join(f"{var}: {val}" for var, val in sorted(values.items())))
# bits = "".join(str(val) for var, val in sorted(values.items(), reverse=True) if var[0] == "z")
# print(bits)
# print(int(bits, base=2))
