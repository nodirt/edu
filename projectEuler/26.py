def period(d):
    n = 1
    i = 0
    nums = {}
    periodLen = 0
    result = ''

    while n:
        i += 1
        if n < d:
            n *= 10
            result += '0'
            continue
        r = n // d
        n %= d
        prevIndex = nums.get(n)
        result += str(r)
        if prevIndex is None:
            nums[n] = i
        else:
            periodLen = i - prevIndex
            break
        n *= 10

    return periodLen

print(max((x, period(x)) for x in range(2, 1000)), key=lambda t: t[1])[0])