import math
import timeit

def main():
	mx = 0

	for x in range(1, 10000):
		y = 0
		t = 10
		dig = [False] * 10
		pandigital = True
		for n in range(1, 10):
			c = x * n

			cd = c
			while cd > 0:
				d = cd % 10
				if dig[d] or d == 0:
					pandigital = False
					break
				dig[d] = True
				cd /= 10

			if not pandigital:
				break

			while t < c:
				t *= 10
			y = y * t + c

			if y > 987654321:
				break
			elif y >= 123456789 and mx < y:
				mx = y
	return mx

print timeit.timeit(main, number=1)