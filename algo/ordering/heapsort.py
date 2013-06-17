import test

def heapsort(nums):
    """Heapsort

    Properties:
        Unstable
        Time: O(n * log(n))
        Space: O(1)

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Heapsort
        Cormen [1]: section 6.4, page 159
        Sedgewick [2]: section 2.4, page 323

    History:
        Author: J. W. J. Williams (1964)
        Williams has invented heapsort, as well as heap.
        The algorithm in heapify_all was suggested by Robert W. Floyd (1964).
    """
    n = len(nums)
    heap_size = n

    def left(i):
        return 2 * i

    def right(i):
        return 2 * i + 1

    def max_heapify(i):
        """Fix max-property invariant if the i-th node key is less than any of its children keys

        Complexity:
            Time: O(log(n/i))
            Space: O(1)

        Assumptions:
            Left and right subtrees of i-th node are heaps
        """
        l = left(i)
        r = right(i)
        if l >= heap_size:
            return
        largest = r if r < heap_size and nums[r] > nums[l] else l
        if nums[largest] > nums[i]:
            nums[i], nums[largest] = nums[largest], nums[i]
            max_heapify(largest)

    for i in xrange(n // 2, -1, -1):
        max_heapify(i)

    # O(n*log(n))
    while heap_size > 0:
        heap_size -= 1
        nums[heap_size], nums[0] = nums[0], nums[heap_size]
        max_heapify(0)


def main():
    test.test_sort(heapsort)
    print('All tests passed')


if __name__ == '__main__':
    main()

