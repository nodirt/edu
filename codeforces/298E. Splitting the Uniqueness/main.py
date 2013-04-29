import math
import sys

def solve(s):
	s = sorted(enumerate(s), key=lambda e: e[1])

	a = [-1] * len(s)
	b = [-1] * len(s)
	dupA = 0
	dupB = 0
	maxDup = math.ceil(float(len(s)) / 3)

	for i, (k, si) in enumerate(s):
		a[k] = si // 2
		b[k] = si - a[k]
		if i == 0:
			continue

		pk, ps = s[i - 1]
		if a[pk] != a[k] and b[pk] != b[k]:
			continue

		if a[k] == b[k]:
			if a[pk] == a[k]:
				dupA += 1
			else:
				dupB += 1
		else:
			swap = False
			if b[pk] != a[k]:
				swap = True
			else:
				if dupA <= dupB:
					dupA += 1
				else:
					dupB += 1
					swap = True

			if swap:
				a[k], b[k] = b[k], a[k]

		if dupA > maxDup or dupB > maxDup:
			return None

	return (a, b)

def solve2(s):
	s = sorted(enumerate(s), key=lambda e: e[1])

	a = [-1] * len(s)
	b = [-1] * len(s)

	dupA = 0
	dupB = 0
	maxDup = math.ceil(float(len(s)) / 3)

	for i, (k, sk) in enumerate(s):
		if i == 0:
			a[k] = 0
		else:
			kp, sp = s[i - 1]
			a[k] = a[kp] + 1

			if sk == sp + 1:
				if dupA <= dupB and dupA < maxDup:
					a[k] = a[kp]
					dupA += 1
				elif b[kp] == sk - a[k]:
					dupB += 1
		b[k] = sk - a[k]

	return (a, b)


def test():	
	print(solve2(range(100, 106)))


def main():
	n = input()
	s = map(int, raw_input().split(' '))
	sol = solve(s)
	if not sol:
		print "NO"
	else:
		a, b = sol
		print "YES"
		print " ".join(map(str, a))
		print " ".join(map(str, b))	


if 'test' in sys.argv:
	test()
else:	
	main()
