import test

def bucket_sort(nums, min=0, max=1):
    """Bucket sort. Sorts floating-point numbers belonging to [min, max) range.

    Properties:
        Stable
        Time: O(n^2). Average: O(n)
        Space: O(n)
        Can be applied to numbers only

    Description:
        Wikipedia: https://en.wikipedia.org/wiki/Bucket_sort
        Cormen [1]: section 8.4, page 200
    """    
    n = len(nums)
    buckets = [[] for i in xrange(n)]
    for x in nums:
        bi = int((x - min) * n / (max - min))
        buckets[bi].append(x)

    for b in buckets:
        for i in xrange(1, len(b)):
            x = b[i]
            j = i
            while j > 0 and b[j - 1] > x:
                b[j] = b[j - 1]
                j -= 1
            b[j] = x
        assert(test.is_sorted(b))

    i = 0
    for b in buckets:
        for x in b:
            nums[i] = x
            i += 1


def main():
    test.test_sort(lambda nums: bucket_sort(nums, 0, 1000))  


if __name__ == '__main__':
    main()
    print('All tests passed')