import test

def counting_sort(items, k, key=None):
    if key is None:
        key = lambda x: x

    count = [0] * k
    for x in items:
        count[key(x)] += 1

    for i in xrange(1, k):
        count[i] += count[i - 1]

    copy = items[:]
    for x in reversed(copy):
        xk = key(x)
        count[xk] -= 1
        assert(count[xk] >= 0)
        items[count[xk]] = x


def main():
    test.test_sort(lambda nums: counting_sort(nums, 1000))
    print('All tests passed')

if __name__ == '__main__':
    main()
