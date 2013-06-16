import math
from counting_sort import counting_sort
import test

def radix_sort(nums):
    d = int(math.log10(max(nums))) + 1
    n = len(nums)
    r = int(math.log(n, 2))
    base = 1 << r
    mask = base - 1
    for i in xrange(d):
        counting_sort(nums, base, key=lambda x: (x >> r * i) & mask)


def main():
    test.test_sort(radix_sort)
    print('All tests passed')

if __name__ == '__main__':
    main()
