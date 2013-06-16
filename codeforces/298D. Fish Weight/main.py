import sys

def solve(a, b):
    a = list(sorted(a, reverse = True))
    b = list(sorted(b, reverse = True))

    neededDiff = 1

    i = 0
    j = 0
    while i < len(a):
        an = 1
        while i + an < len(a) and a[i + an] == a[i]:
            an += 1

        bn = 0
        while j + bn < len(b) and b[j + bn] >= a[i]:
            bn += 1

        diff = an - bn
        if diff >= neededDiff:
            return True
        else:
            neededDiff -= diff

        i += an
        j += bn

    return False


if 'test' in sys.argv:
    a = [2, 2, 2]
    b = [1, 1, 3]
    assert(solve(a, b))

    a = [5, 2, 7, 3]
    b = [3, 5, 2, 7, 3, 8, 7]
    assert(not solve(a, b))
else:
    n = raw_input()
    a = [int(x) for x in raw_input().split(' ')]
    b = [int(x) for x in raw_input().split(' ')]
    print 'YES' if solve(a, b) else 'NO'