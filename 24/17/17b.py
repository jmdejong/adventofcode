#!/usr/bin/python3


def calc(a):
	# r = []
	z = 0
	while a > 0:
		d = a & 0b111 ^ 0b101
		e = d ^ 0b110 ^ (a >> d) & 0b111
		z = z * 8 | e
		# r.append(e)
		a = a >> 3
	return z
	# return r

def inv(out):
	# for o in out:
	a = 0
	# for o in reversed(out):
	for jj in range(len(out)):
		j = len(out) - jj - 1
		part = out[j:]
		o = part[0]
		print(f"j: {j}, o: {o}, a: {a}")
		a = a * 8
		for i in range(8):
			print(i, a, o)
			if calc(i | a) == part:
				a |= i
				break
		else:
			print(f"impossible")
			break
	return a
	# return o ^ 0b011

def rinv(target, a=0):
	if target == 0:
		return a
	o = target % 8
	print(target, a, o)
	target = target // 8
	# out = take_apart(target)
	# o = out[-1]
	# target = build(out[:-1])
	a = a * 8
	for i in range(8):
		c = calc(i | a) % 8
		if c == o:
			# print(target, i, i | a)
			r = rinv(target, i | a)
			if r != None:
				print(r)
				return r

def rinv3(code, ptr, a):
	if calc(a) != build(code[ptr:]):
		return None
	if ptr == 0:
		return a
	for i in range(8):
		r = rinv3(code, ptr-1, (a*8)|i)
		if r != None:
			return r
	else:
		print("impossible")


def _rinv(out, a, found):
	if len(out) == 0:
		return a
	# o = out[-1]
	# rest = out[:-1]
	a *= 8
	o = out[0]
	out = out[1:]
	found = found + [o]
	for i in range(8):
		if calc(i | a) == found:
			r = rinv(rest, i | a)
			if r != None:
				return r


def take_apart(n):
	r = []
	while n > 0:
		r.append(n%8)
		n //= 8
	return list(reversed(r))

def build(code):
	z = 0
	for op in code:
		z = z * 8 | op
	return z

print(",".join(str(num) for num in take_apart(calc(61156655))))


source_code = [2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0]
target = build(source_code)

for i in range(0):
	c = take_apart(calc(i))
	code = source_code[len(source_code) - len(take_apart(i)):]
	if c == code:
		# print(take_apart(i))
		print(i)
		# print(c)

print(calc(0))

print("\n")

code = source_code#[5,3,0]
# target = 61 #target & 0b111_111
# a = rinv(target)
a = rinv3(code, len(code), 0)
print("")
print(a)
if a == None:
	print("calc a failed")
	exit(-1)
print("")
print(calc(a))
print(build(code))
print(take_apart(calc(a)))
print(code)

# for i in range(100):
	# print(i, take_apart(calc(i)))
# print(take_apart(calc(a)))
# print(take_apart(target))
# a = take_apart(target)
# print(source_code)
# print(a)
# print(target)
# print(build(a))

# # for i in range(8):
# 	# print(i, inv([i]), calc(inv([i])))
# v = rinv(source_code)
# print(source_code)
# print(v)
# print(calc(v))
# # for i in range(1,len(source_code)):
# 	# c = source_code[-i:]
# 	# v = inv(c)
# 	# print(c, v, calc(v))
# 	# print("")
