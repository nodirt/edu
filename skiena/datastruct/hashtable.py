import random
from timeit import timeit
from time import sleep

class Entry:
    def __init__(self, key, value, hashCode):
        self.key = key
        self.value = value
        self.hashCode = hashCode


_primes = [2, 3, 5]

def binarySearch(lst, elem):
    l = 0
    r = len(lst)

    if l >= r:
        return ~l

    while l < r:
        m = (l + r - 1) // 2
        if lst[m] == elem:
            return m
        elif lst[m] > elem:
            r = m
        else:
            l = m + 1

    return ~r


def nextPrime(x):
    if _primes[-1] >= x:
        i = binarySearch(_primes, x)
        return _primes[i if i >= 0 else ~i]


    p = _primes[-1]
    while True:
        p += 1
        isPrime = True
        for sp in _primes:
            if p % sp == 0:
                isPrime = False
                break

        if isPrime:
            _primes.append(p)
            if p >= x:
                return p

nextPrime(1000)

class Hashtable:
    def __init__(self, size=13, hashFn=hash):
        self._entries = [None] * nextPrime(size)
        self._capacity = len(self._entries)
        self._count = 0
        self.hashFn = hashFn


    def __len__(self):
        return self._count

    def _find(self, key, hashCode=None):
        if hashCode is None:
            hashCode = self.hashFn(key)
        i = hashCode % self._capacity
        while True:
            e = self._entries[i]
            if not e:
                break
            if e.hashCode == hashCode and e.key == key:
                return i
            i = (i + 1) % self._capacity
        return ~i

    def _put(self, key, value, allowDuplicate=False):
        if self._count * 3 >= self._capacity:
            self._enlarge()

        hashCode = self.hashFn(key)
        i = self._find(key, hashCode)
        if i >= 0:
            if not allowDuplicate:
                raise KeyError('Key is already present')
            self._entries[i].value = value
        else:
            self._entries[~i] = Entry(key, value, hashCode)
            self._count += 1

    def __getitem__(self, key):
        i = self._find(key)
        if i < 0:
            raise KeyError('Key not found')
        return self._entries[i].value

    def __setitem__(self, key, value):
        return self._put(key, value, True)

    def add(self, key, value):
        self._put(key, value)

    def __contains__(self, key):
        return self._find(key) >= 0

    def _reinsert(self, entries):
        for e in entries:
            if not e:
                continue
            i = self._find(e.key, e.hashCode)
            assert(i < 0)
            self._entries[~i] = e        
        
    def _enlarge(self):
        print('Enlarge')
        self._capacity = nextPrime(self._capacity * 2)
        oldEntries = self._entries
        self._entries = [None] * self._capacity
        self._reinsert(oldEntries)

    def __delitem__(self, key):
        i = self._find(key)
        if i < 0:
            raise KeyError('Key not found')

        toInsert = []
        while True:
            self._entries[i] = None
            i = (i + 1) % self._capacity
            if not self._entries[i]:
                break
            toInsert.append(self._entries[i])

        self._count -= 1
        self._reinsert(toInsert)

    def clear(self):
        for i in range(self._capacity):
            self._entries[i] = None
        self._count = 0


class Node(object):
    def __init__(self, key, value, hashCode, next=None):
        self.key = key
        self.value = value
        self.hashCode = hashCode
        self.next = next


class LinkedEntry(object):
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, node):
        if self.last:
            self.last.next = node
            self.last = node
        else:
            self.last = node
            self.first = node


class LinkedHashtable(object):
    def __init__(self, size=13, hashFn=hash):
        self._entries = [None] * nextPrime(size)
        self._capacity = len(self._entries)
        self._count = 0
        self.hashFn = hashFn


    def __len__(self):
        return self._count

    def _find(self, key, hashCode=None):
        if hashCode is None:
            hashCode = self.hashFn(key)
        i = hashCode % self._capacity
        lst = self._entries[i]
        if not lst:
            return None
        node = lst.first
        while node:
            if node.hashCode == hashCode and node.key == key:
                return node
            node = node.next
        return None

    def _put(self, key, value, allowDuplicate=False):
        if self._count * 3 >= self._capacity:
            self._enlarge()

        hashCode = self.hashFn(key)
        i = hashCode % self._capacity
        lst = self._entries[i]
        if not lst:
            lst = LinkedEntry()
            self._entries[i] = lst 

        addNew = True
        n = lst.first
        while n:
            if n.hashCode == hashCode and n.key == key:
                if not allowDuplicate:
                    raise KeyError('Key is already present')
                n.value = value
                addNew = False
                break
            n = n.next

        if addNew:
            lst.append(Node(key, value, hashCode))
            self._count += 1

    def __getitem__(self, key):
        node = self._find(key)
        if not node:
            self._keyNotFound(key)
        return node.value

    def __setitem__(self, key, value):
        return self._put(key, value, True)

    def add(self, key, value):
        self._put(key, value)

    def __contains__(self, key):
        return self._find(key) is not None
    
    def _enlarge(self):
        # print('Enlarge')
        self._capacity = nextPrime(self._capacity * 2)
        oldEntries = self._entries
        self._entries = [None] * self._capacity
        for lst in oldEntries:
            if not lst:
                continue
            n = lst.first
            while n:
                i = n.hashCode % self._capacity
                if not self._entries[i]:
                    self._entries[i] = LinkedEntry()
                next = n.next
                n.next = None
                self._entries[i].append(n)
                n = next

    def _keyNotFound(self, key):
        raise KeyError('Key not found: %s' % key)

    def __delitem__(self, key):
        hashCode = self.hashFn(key)
        i = hashCode % self._capacity
        lst = self._entries[i]
        if not lst:
            self._keyNotFound()
        node = lst.first
        if node.hashCode == hashCode and node.key == key:
            lst.first = node.next
            if lst.last == node:
                lst.last = node.next
        else:
            found = False
            while node.next:
                if node.next.hashCode == hashCode and node.next.key == key:
                    if lst.last == node.next:
                        lst.last = node.next
                    node.next = node.next.next
                    found = True
                    break
                node = node.next

            if not found:
                self._keyNotFound(key)

        self._count -= 1

    def clear(self):
        for i in range(self._capacity):
            self._entries[i] = None
        self._count = 0



def test():
    mx = 100
    def randint():
        return random.randint(0, mx)
    def randrange():
        population = list(range(mx))
        return random.sample(population, random.randint(0, len(population)))

    def compare(dictOp, tableOp, number):
        num = 10000
        dictTime = timeit(dictOp, number=number)
        tableTime = timeit(tableOp, number=number)
        if tableTime * 2 > dictTime:
            factor = tableTime / dictTime
            print('%s is slow: %f' % (tableOp.func_name, factor))
            if factor > 20:
                sleep(1)


    for testCase in range(100):
        d = dict()
        t = LinkedHashtable()

        def testState():
            print('Tests')
            assert(len(d) == len(t))
            for k, v in d.items():
                assert(k in t)
                assert(t[k] == v)
            for k in randrange():
                assert((k in d) == (k in t))

            if type(t) == Hashtable:
                assert(sum(1 for e in t._entries if e) == len(t))

        # print 'Insert'
        for k in randrange():
            v = randint()
            def insDict():
                d[k] = v
            def insTable():
                t[k] = v
            print('Insert %s' % k)
            compare(insDict, insTable, 1)
            testState()

        for k in list(d.keys()):
            def delDict():
                del d[k]
            def delTable():
                del t[k]
            compare(delDict, delTable, 1)
            testState()

        print('========== Test %d passed ==========' % testCase)


if __name__ == '__main__':
    test()
