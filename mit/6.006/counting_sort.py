def counting_sort(nums, k):
	count = [0] * (k + 1)
	for x in nums:
		count[x] += 1

	for i in xrange(1, k + 1):
		count[i] += count[i - 1]

	result = [0] * len(nums)
	for x in reversed(nums):
		count[x] -= 1
		result[count[x]] = x
		assert(count[x] >= 0)

	return result


def main():
	def test_sort(array):
		array = counting_sort(array, 10)
		print(array)
		for i in xrange(1, len(array)):
			assert(array[i - 1] <= array[i])

	test_sort([0, 1, 2, 0, 3, 2, 1])
	test_sort([0, 1, 1, 0, 1, 1, 1])
	test_sort([0] * 10)
	test_sort(range(10))
	test_sort(range(10, -1, -1))
	print('All tests passed')

if __name__ == '__main__':
	main()
