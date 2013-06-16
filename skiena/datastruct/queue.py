class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue(object):
    def __init__(self, items=None):
        self.head = Node(None)
        self.last = None
        self.size = 0
        if items:
            for x in items:
                self.enqueue(x)

    def __len__(self):
        return self.size

    def enqueue(self, value):
        node = Node(value)
        if self.last:
            self.last.next = node
        else:
            self.head.next = node
        self.last = node
        self.size += 1
        return self

    def __iter__(self):
        n = self.head.next
        while n:
            yield n.value
            n = n.next

    def dequeue(self):
        if not self.head.next:
            raise ValueError('Queue is empty')
        value = self.head.next.value
        if self.last == self.head.next:
            self.last = None
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if not self.head.next:
            raise ValueError('Queue is empty')
        return self.head.next.value

    def __contains__(self, value):
        n = self.head.next
        while n:
            if n.value == value:
                return True
            n = n.next
        return False


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1).enqueue(2).enqueue(3)
    assert(q)
    assert(len(q) == 3)
    assert(q.dequeue() == 1)
    assert(len(q) == 2)
    assert(q.dequeue() == 2)
    assert(len(q) == 1)
    assert(q)
    q.enqueue(4)
    assert(len(q) == 2)
    assert(q.dequeue() == 3)
    assert(len(q) == 1)
    assert(q)
    assert(q.dequeue() == 4)
    assert(len(q) == 0)
    assert(not q)
    print('All tests passed')