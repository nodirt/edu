import random

def is_sorted(array):
    for i in xrange(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True

def test_sort(fn):
    array = range(100)
    for i in xrange(100):
        random.shuffle(array)
        fn(array)
        assert(is_sorted(array))

    for i in xrange(100):
        array = [random.randint(0, 100) for x in xrange(1000)]
        fn(array)
        assert(is_sorted(array))

