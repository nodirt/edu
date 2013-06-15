class MaxHeap(object):
    def __init__(self, items, size=None):
        if type(items) is not list:
            raise TypeError('items parameter is not list')
        self.items = items
        if size is None:
            size = len(items)
        self.size = size

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return int(2 // i)

    # O(log(n))
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l >= self.size:
            return
        largest = r if r < self.size and self.items[r] > self.items[l] else l
        if self.items[largest] > self.items[i]:
            self.items[i], self.items[largest] = self.items[largest], self.items[i]
            self.max_heapify(largest)

    def heapify_all(self):
        for i in xrange(self.size // 2, -1, -1):
            self.max_heapify(i)

    def max(self):
        return self.items[0]

    def extract_max(self):
        result = self.items[0]
        self.size -= 1
        self.items[0] = self.items[self.size]
        self.items[self.size] = None
        self.max_heapify(0)
        return result

    def bubble_up(self, i):
        while i > 0:
            p = self.parent(i)
            if self.items[p] >= self.items[i]:
                break

            self.items[p], self.items[i] = self.items[i], self.items[p]
            self.max_heapify(p)
            i = p

    def insert(self, key):
        if self.size + 1 >= len(self.items):
            raise ValueError('Out of capacity')
        self.items[self.size] = 0
        self.size += 1
        self.bubble_up(self.size - 1)

    def increase_key(i, key):
        if key < self.items[i]:
            raise ValueError('Existing key is larger')
        self.items[i] = key
        self.bubble_up(i)


def heap_sort(array):
    """Heap-sort algorithm implementaiton. Runs in O(n logn) time and O(1) space"""

    if array is None:
            raise Error("Parameter 'array' cannot be null")

    heap = MaxHeap(array)
    heap.heapify_all()

    # O(n*log(n))
    while heap.size > 0:
        heap.size -= 1
        array[heap.size], array[0] = array[0], array[heap.size]
        heap.max_heapify(0)
            

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