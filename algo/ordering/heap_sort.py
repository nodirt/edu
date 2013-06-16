import operator
from heap import Heap
import test

def heap_sort(array):
    """Heap-sort algorithm implementaiton. Runs in O(n logn) time and O(1) space"""

    if array is None:
            raise Error("Parameter 'array' cannot be null")

    heap = Heap(array)
    heap.heapify_all()

    # O(n*log(n))
    while heap.size > 0:
        heap.size -= 1
        array[heap.size], array[0] = array[0], array[heap.size]
        heap.max_heapify(0)


def main():
    test.test_sort(heap_sort)
    print('All tests passed')

if __name__ == '__main__':
    main()

