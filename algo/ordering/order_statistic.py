"""Find i-th smallest element in the array

Complexity:
    Time: O(n^2). Average: O(n)
    Space: O(n). Average: O(log(n))

Description:
    Wikipedia: http://en.wikipedia.org/wiki/Order_statistic
    Cormen [1]: section 9.2, page 216

History:
    Author: Hoare (1961)
    Hoare is author of quicksort
"""
import random


def order_statistic_recursive(array, order):
    if order < 0 or order >= len(array):
        raise ValueError('Order must be between 0 and len(array) - 1')

    def find(lo, hi, order):
        assert(order >= 0 and order <= hi - lo)
        if lo >= hi:
            return array[lo]

        p = array[lo + (hi - lo) // 2]
        i = lo
        j = hi
        while i <= j:
            while array[i] < p:
                i += 1
            while array[j] > p:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        left_partition_size = j - lo + 1
        if left_partition_size == order:
            return p
        elif left_partition_size > order:
            return find(lo, j, order)
        else:
            return find(i, hi, order - left_partition_size - 1)

    return find(0, len(array) - 1, order)


def order_statistic_iterative(array, order):
    if order < 0 or order >= len(array):
        raise ValueError('Order must be between 0 and len(array) - 1')

    lo = 0
    hi = len(array) - 1
    while True:
        if lo >= hi:
            assert(order == 0)
            return array[lo]

        p = array[lo + (hi - lo) // 2]
        i = lo
        j = hi
        while i <= j:
            while array[i] < p:
                i += 1
            while array[j] > p:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        left_partition_size = j - lo + 1
        if left_partition_size == order:
            return p
        elif left_partition_size > order:
            hi = j
        else:
            lo = i
            order -= left_partition_size + 1


def main():
    def test(fn):
        n = 100
        array = range(n)
        random.shuffle(array)
        for i in xrange(n):
            assert(fn(array, i) == i)

    test(order_statistic_recursive)
    test(order_statistic_iterative)

    print('All tests passed')


if __name__ == '__main__':
    main()
