import test


def selection_sort(nums):
    """Selection sort.

    Properties:
        Unstable
        Time: O(n^2)
        Space: O(1)
        Swaps: O(n), optimal
        Comparisons: O(n^2)

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Selection_sort
        Sedgewick [2]: section 2.1, page 248
    """
    n = len(nums)
    for i in xrange(n):
        smallest = i
        for j in xrange(i + 1, n):
            if nums[j] < nums[smallest]:
                smallest = j

        nums[i], nums[smallest] = nums[smallest], nums[i]


def main():
    test.test_sort(selection_sort)
    print('All tests passed')


if __name__ == '__main__':
    main()