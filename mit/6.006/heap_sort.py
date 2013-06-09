def heap_sort(array):
    """Heap-sort algorithm implementaiton. Runs in O(n logn) time and O(1) space"""

    if array is None:
            raise Error("Parameter 'array' cannot be null")

    # O(log(n-i))
    def max_heapify(array, n, i):
        left = 2 * i
        right = left + 1
        largest = i
        if left < n:
            if array[left] > array[largest]:
                largest = left
            if right < n and array[right] > array[largest]:
                largest = right
        if largest > i:
            array[i], array[largest] = array[largest], array[i]
            max_heapify(array, n, largest)

    n = len(array)
    # O(n)
    for i in xrange(n/2, -1, -1):
        max_heapify(array, n, i)

    # O(n*log(n))
    while n > 0:
        n -= 1          
        array[0], array[n] = array[n], array[0]
        max_heapify(array, n, 0)    
            

def test():
    def test_heap_sort(array):
        expected = list(sorted(array))
        heap_sort(array)
        assert(array == expected)

    test_heap_sort([4, 2, 1])
    test_heap_sort([4, 1, 2, 1])
    test_heap_sort([])

    print('All tests passed')

if __name__ == '__main__':
    test()