import math

def p(n):
	return n * (3 * n - 1) // 2

def is_pentagonal(px):
	x = (1 + math.sqrt(1 + 24 * px)) / 6
	return int(x) == x


def solve():
	s = 1
	while True:
		ps = p(s)
		d = 1
		while d < s:
			pd = p(d)
			if (pd + ps) % 2 == 0:
				pk = int((ps + pd) // 2)
				if is_pentagonal(pk) and is_pentagonal(ps - pk):
					return ((d, pd), pk, (s, ps))

			d += 1
		s += 1

print(solve())