def find_max_subarray(array):
    """Find maximum subarray in an array

    Description:
        Cormen [1]: section 4.1, page 70

    History:
        Author: Bentley (1986)
    """
    if type(array) != list:
        raise Exception('List expected')

    def find_cross(low, mid, high):
        """O(high - mid)"""
        left = 0
        left_sum = 0
        cur_sum = 0
        for i in xrange(mid, low - 1, -1):
            cur_sum += array[i]
            if cur_sum > left_sum:
                left_sum = cur_sum
                left = i

        right = 0
        right_sum = 0
        cur_sum = 0
        for i in xrange(mid + 1, high + 1):
            cur_sum += array[i]
            if cur_sum > right_sum:
                right_sum = cur_sum
                right = i

        return (left, right, left_sum + right_sum)

    def find(low, high):
        """O(n * log(n)), where n = high - low"""
        if low >= high:
            return (low, low, array[low])
        mid = low + int((high - low) // 2)
        low_res = find(low, mid)
        cross_res = find_cross(low, mid, high)
        high_res = find(mid + 1, high)
        low_sum, cross_sum, high_sum = low_res[2], cross_res[2], high_res[2]
        if low_sum >= cross_sum and low_sum >= high_sum:
            return low_res
        elif cross_sum > high_sum:
            return cross_res
        else:
            return high_res

    return find(0, len(array) - 1)
            

def test():
    def test_max_subarray(array, expected):
        left, right, max_sum = find_max_subarray(array)
        actual = array[left:right + 1]
        assert(actual == expected)

    test_max_subarray([1, -2, 1, 4, -3], [1, 4])
    test_max_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], [18, 20, -7, 12])

if __name__ == '__main__':
    test()
