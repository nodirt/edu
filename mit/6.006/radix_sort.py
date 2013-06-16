from counting_sort import counting_sort, is_sorted

def radix_sort(nums, d):
	m = 1
	for i in xrange(d):
		counting_sort(nums, 10, key=lambda x: (x // m) % 10)
		m *= 10


def main():
	def test_sort(array):
		radix_sort(array, 2)
		assert(is_sorted(array))

	test_sort([02, 11, 27, 20, 35, 12, 51])
	test_sort([0] * 10)
	test_sort(range(100))
	test_sort(range(99, -1, -1))
	print('All tests passed')

if __name__ == '__main__':
	main()
