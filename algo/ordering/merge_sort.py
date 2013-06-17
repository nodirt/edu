import test


def merge_sort(nums):
    """Merge sort. Divide & Conquer approach.

    Properties:
        Stable
        Time: O(n * log(n))
        Space: O(n)
        Does not require random access
        Can be applied to sort data stored on external devices

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Merge_sort
        Cormen [1]: section 2.3, page 30
        Sedgewick [2]: section 2.2, page 270

    History:
        Author: John von Neumann (1945)
    """
    n = len(nums)
    aux = [0] * n

    def sort(lo, hi):
        if lo >= hi:
            return

        half = lo + (hi - lo) // 2
        sort(lo, half)
        sort(half + 1, hi)

        if nums[half] <= nums[half + 1]:
            # it is already sorted
            return

        i = lo
        j = half + 1
        k = 0
        while i <= half and j <= hi:
            if nums[i] <= nums[j]:
                aux[k] = nums[i]
                i += 1
            else:
                aux[k] = nums[j]
                j += 1
            k += 1

        if i <= half:
            # something remains on the left. Move it right
            assert(nums[i] >= nums[hi])
            remains_count = half - i + 1
            for i in xrange(remains_count):
                nums[hi - i] = nums[half - i]

        for i in xrange(k):
            nums[lo + i] = aux[i]

    sort(0, n - 1)


def main():
    test.test_sort(merge_sort)
    print('All tests passed')


if __name__ == '__main__':
    main()