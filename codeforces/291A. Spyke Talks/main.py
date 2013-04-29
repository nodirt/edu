import sys

def solve(sessions):
	count = 0
	prev = -1
	prevRep = False
	for x in sorted(sessions):
		if x == 0:
			continue

		if x == prev:
			if prevRep:
				return -1
			prevRep = True
			count += 1
		else:
			prevRep = False

		prev = x

	return count


if 'test' in sys.argv:
	assert(solve([0, 1, 7, 1, 7, 10]) == 2)
	assert(solve([1, 1, 1]) == -1)
	assert(solve([0]) == 0)
	assert(solve([0, 1]) == 0)
	assert(solve([2, 1]) == 0)
	assert(solve([2, 2]) == 1)
	print 'Passed'
else:
	n = input()
	print solve(int(x) for x in raw_input().split(' '))