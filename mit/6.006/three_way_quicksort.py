import test

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
	test.test_sort(three_way_quicksort)
	print('All tests passed')

if __name__ == '__main__':
	main()
