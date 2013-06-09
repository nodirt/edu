import math

def solve(h=1):
	while True:
		x = 2 * h * (2 * h - 1)
		n = (1 + math.sqrt(1 + 12 * x)) / 6
		t = (-1 + math.sqrt(1 + 4 * x)) / 2
		if n == int(n) and t == int(t):
			return x // 2

		h += 1

print(solve(145))