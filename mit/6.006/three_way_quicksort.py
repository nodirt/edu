def three_way_quicksort(nums):
	def sort(lo, hi):
		if lo >= hi:
			return
		lt = lo - 1 # last x < p
		i = lo # current number
		gt = hi + 1 # first x > p
		p = nums[lo + (hi - lo) // 2]
		while i < gt:
			x = nums[i]
			if x < p:
				lt += 1
				nums[lt], nums[i] = nums[i], nums[lt]
				i += 1
			elif x > p:
				gt -= 1
				nums[gt], nums[i] = nums[i], nums[gt]
			else:
				i += 1

		sort(lo, lt)
		sort(gt, hi)

	sort(0, len(nums) - 1)


def main():
	def test_sort(array):
		three_way_quicksort(array)
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
