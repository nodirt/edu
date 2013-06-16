import math
from counting_sort import counting_sort
import test

def radix_sort(nums):
	d = int(math.log10(max(nums))) + 1

	m = 1
	base = len(nums)
	for i in xrange(d):
		counting_sort(nums, base, key=lambda x: (x // m) % base)
		m *= base


def main():
	test.test_sort(radix_sort)
	print('All tests passed')

if __name__ == '__main__':
	main()
