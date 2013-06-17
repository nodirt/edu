import test


def counting_sort(items, k):
    """Counting sort, sorts integers from 0 to k - 1.

    Properties:
        Stable
        Time: O(n + k)
        Space: O(n + k)
        Can be applied to integers only

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Counting_sort
        Cormen [1]: section 8.2, page 194

    History:
        Author: Harold H. Seward (1954)
        Although radix sorting itself dates back far longer, counting sort, and its application to radix sorting, were both invented by Harold H. Seward in 1954.

    """
    count = [0] * k
    for x in items:
        count[x] += 1

    for i in xrange(1, k):
        count[i] += count[i - 1]

    copy = items[:]
    for x in reversed(copy):
        count[x] -= 1
        assert(count[x] >= 0)
        items[count[x]] = x


def main():
    test.test_sort(lambda nums: counting_sort(nums, 1000))
    print('All tests passed')


if __name__ == '__main__':
    main()
