import random

def mergesort(nums, start, end):
    if start >= end:
        return [nums[start]] if start < len(nums) else []
    mid = start + (end - start + 1) // 2
    a = mergesort(nums, start, mid - 1)
    b = mergesort(nums, mid, end)
    result = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        moveI = True
        if i >= len(a):
            moveI = False
        elif j >= len(b):
            moveI = True
        else:
            moveI = a[i] < b[j]

        if moveI:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result


for i in range(0, 100):
    nums = list(range(0, random.randint(0, 30)))
    random.shuffle(nums)

    expected = list(sorted(nums))
    actual = mergesort(nums, 0, len(nums) - 1)
    assert(expected == actual)
