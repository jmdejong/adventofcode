#!/usr/bin/python3
import sys

snafu_digits = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
snafu_inverse = {val: key for key, val in snafu_digits.items()}

def parse_snafu(snafu):
	n = 0
	for c in snafu:
		n *= 5
		n += snafu_digits[c]
	return n

def to_snafu(num):
	chars = []
	while num != 0:
		rem = num % 5
		if rem > 2:
			rem -= 5
			num += 5
		chars.append(snafu_inverse[rem])
		num //= 5
	return "".join(reversed(chars))

fuel = sum(parse_snafu(line.strip()) for line in open(sys.argv[1]))
print(fuel)
print(to_snafu(fuel))
# for line in open(sys.argv[1]):
	# print(parse_snafu(line.strip()))
