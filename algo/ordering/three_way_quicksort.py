import test

def three_way_quicksort(nums):
    """3-way quicksort, works much faster than original quicksort when input contains duplicates.

    Complexity:
        Time: O(n*n)
        Average time: O(n * log(n))
        Space: O(1)

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Quicksort#Variants
        Sedgewick [2]: section 2.3, page 296

    History:
        Author: Sedgewick (1970s)
        Was improved by J. Bentley and D. McIlroy in 1990s and got popularity
    """
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
