maxP = 1000

sq = [x * x for x in range(maxP)]

def squareOf(x):
    left = 0
    right = len(sq)
    while left < right:
        mid = left + (right - left) // 2
        p = sq[mid]
        if p == x:
            return mid
        elif x < p:
            if mid <= 0:
                break
            right = mid
        else:
            if mid >= right - 1:
                break
            left = mid + 1
    return None

def testSearch():
    for x in range(maxP * maxP):
        assert(squareOf(x) is not None == (x in sq))


# testSearch()

sol = [0] * maxP

for a in range(1, maxP // 2):
    asq = sq[a]
    for b in range(a + 1, maxP // 2 - a):
        bsq = sq[b]

        csq = asq + bsq

        c = squareOf(asq + bsq)
        if c is None:
            continue

        p = a + b + c
        sol[p] += 1


print(max(range(maxP), key=lambda i: sol[i]))
