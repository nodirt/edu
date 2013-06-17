import operator
from heap import Heap
import test

def heap_sort(array):
    """Heapsort

    Complexity:
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

