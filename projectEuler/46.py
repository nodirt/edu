import math
import nums

def check(x):
	for p in nums.primes(x):
		if p == x:
			return True
		y = math.sqrt((x - p) / 2)
		if y == int(y):
			return True

	return False

def solve():
	x = 33
	while True:
		if not check(x):
			return x
		x += 2

print(solve())
