import operator
import test

class Heap(object):
    def __init__(self, items, size=None, cmpFn=None):
        if type(items) is not list:
            raise TypeError('items parameter is not list')
        self.items = items

        if size is None:
            size = len(items)
        self.size = size

        self.cmp = cmpFn or cmp

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return int(i // 2)

    def compare(self, i, j):
        return self.cmp(self.items[i], self.items[j])

    # O(log(n))
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l >= self.size:
            return
        largest = r if r < self.size and self.compare(r, l) > 0 else l
        if self.compare(largest, i) > 0:
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
            if self.compare(p, i) >= 0:
                break

            self.items[p], self.items[i] = self.items[i], self.items[p]
            self.max_heapify(p)
            i = p

    def insert(self, key):
        if self.size >= len(self.items):
            raise ValueError('Out of capacity')
        self.items[self.size] = key
        self.size += 1
        self.bubble_up(self.size - 1)

    def increase_key(i, key):
        if key < self.items[i]:
            raise ValueError('Existing key is larger')
        self.items[i] = key
        self.bubble_up(i)

    def delete(self, i):
        if i < 0 or i >= self.size:
            raise ValueError('Incorrect index')
        self.size -= 1
        self.items[i] = self.items[self.size]
        self.items[self.size] = None
        self.max_heapify(i)


# merge descending ordered lists
def merge_lists(lists):
    def cmpLists(a, b):
        al, ai = a
        bl, bi = b
        return cmp(bl[bi], al[ai])


    queue = Heap(
        [(l, 0) for l in lists if l],
        cmpFn=cmpLists
    )
    queue.heapify_all()

    while queue.size > 0:
        l, i = queue.extract_max()
        yield l[i]

        i += 1
        if i < len(l):
            queue.insert((l, i))


def main():
    def test_merge_lists(a, b, c, merged):
        assert(merged == list(merge_lists([a, b, c])))

    test_merge_lists([2, 4], [1, 6], [3, 5], [1, 2, 3, 4, 5, 6])

    print('All tests passed')

if __name__ == '__main__':
    main()

