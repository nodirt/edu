import math
import test

def radix_sort(nums):
    """Radix sort

    Properties:
        Stable
        Time: O(n)
        Space: O(n + k)

    Author: Tony Hoare (1960)

    Description:
        Wikipedia: https://en.wikipedia.org/wiki/Radix_sort
        Cormen [1]: section 7, page 170

    History:
        Author: Harold H. Seward (1954), MIT
        Although radix sorting itself dates back far longer, counting sort, and its application to radix sorting, were both invented by Harold H. Seward in 1954 at MIT.
    """
    n = len(nums)
    r = min(1, int(math.log(n, 2)))
    base = 1 << r
    mask = base - 1
    count = [0] * base
    buf = [0] * n
    s = 0
    while True:
        fin = True
        for x in nums:
            key = x >> s
            if key != 0:
                fin = False
            key &= mask
            count[key] += 1

        if fin:
            break

        for i in xrange(1, base):
            count[i] += count[i - 1]

        for x in reversed(nums):
            key = (x >> s) & mask
            count[key] -= 1
            assert(count[key] >= 0)
            buf[count[key]] = x

        for i in xrange(n):
            nums[i] = buf[i]

        # cleanup
        for i in xrange(base):
            count[i] = 0

        s += r


def main():
    test.test_sort(radix_sort)
    print('All tests passed')

if __name__ == '__main__':
    main()
