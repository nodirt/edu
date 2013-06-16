def counting_sort(items, k, key=None):
	if key is None:
		key = lambda x: x

	count = [0] * k
	for x in items:
		count[key(x)] += 1

	for i in xrange(1, k):
		count[i] += count[i - 1]

	copy = items[:]
	for x in reversed(copy):
		xk = key(x)
		count[xk] -= 1
		assert(count[xk] >= 0)
		items[count[xk]] = x


def is_sorted(array):
	for i in xrange(1, len(array)):
		if array[i - 1] > array[i]:
			return False
	return True


def main():
	def test_sort(array):
		counting_sort(array, 10)
		assert(is_sorted(array))

	test_sort([0, 1, 2, 0, 3, 2, 1])
	test_sort([0, 1, 1, 0, 1, 1, 1])
	test_sort([0] * 10)
	test_sort(range(9))
	test_sort(range(9, -1, -1))
	print('All tests passed')

if __name__ == '__main__':
	main()
