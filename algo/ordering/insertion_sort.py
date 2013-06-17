import test

def insertion_sort(nums):
    """Insertion sort. Suitable for small arrays or nearly sorted arrays.

    Properties:
        Stable
        Time: O(n^2)
        Space: O(1)
        Adaptive: O(n) time when nearly sorted
        Very low overhead

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Insertion_sort
        Cormen [1]: section 2.1, page 16
        Sedgewick [2]: section 2.1, page 250
    """
    n = len(nums)
    for i in xrange(1, n):
        x = nums[i]
        j = i
        while j > 0 and nums[j - 1] > x:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = x


def main():
    test.test_sort(insertion_sort)
    print('All tests passed')


if __name__ == '__main__':
    main()
