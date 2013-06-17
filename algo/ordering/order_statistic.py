import random

def order_statistic(array, i):
    """Find ith smallest element in the array

    Complexity:
        Time: O(n * log(n))
        Average time: O(n)
        Space: O(1)

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Order_statistic
        Cormen [1]: section 9.2, page 216
    """

    if i < 0 or i >= len(array):
        raise ValueError('Order must be between 0 and len(array) inclusive')

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

    return find(0, len(array) - 1, i)


def main():
    n = 100
    array = range(n)
    random.shuffle(array)
    for i in xrange(n):
        assert(order_statistic(array, i) == i)
    print('All tests passed')


if __name__ == '__main__':
    main()