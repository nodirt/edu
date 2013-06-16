import random

class MinHeap:
    def __init__(self, values=None):
        self.q = []
        if values:
            self.q += values
            for i in range(len(self.q) - 1, -1, -1):
                self.bubbleDown(i)


    def add(self, x):
        self.q.append(x)
        self.bubbleUp(len(self.q) - 1)

    def isEmpty(self):
        return not bool(self.q)

    def extractMin(self):
        result = self.q[0]
        last = self.q.pop(-1)
        if self.q:
            self.q[0] = last
            self.bubbleDown(0)
        return result

    def bubbleUp(self, i):
        parent = self.parent(i)
        if parent == -1:
            return
        if self.q[parent] > self.q[i]:
            self.swap(parent, i)
            self.bubbleUp(parent)

    def bubbleDown(self, i):
        leftChild = self.leftChild(i)
        minChild = i
        for j in range(0, 2):
            child = leftChild + j
            if child < len(self.q) and self.q[child] < self.q[minChild]:
                minChild = child

        if minChild != i:
            self.swap(i, minChild)
            self.bubbleDown(minChild)

    def parent(self, i):
        return (i + 1) // 2 - 1 if i >= 1 else -1

    def leftChild(self, i):
        return (i + 1) * 2 - 1

    def swap(self, i, j):
        self.q[i], self.q[j] = self.q[j], self.q[i]


def heapSort(items):
    heap = MinHeap()
    for x in items:
        heap.add(x)
    items[:] = []
    while not heap.isEmpty():
        items.append(heap.extractMin())

for i in range(0, 100):
    nums = list(range(0, random.randint(0, 30)))
    random.shuffle(nums)

    expected = list(sorted(nums))
    actual = nums
    heapSort(actual)
    assert(expected == actual)
