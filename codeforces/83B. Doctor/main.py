import sys

class Animal:
    def __init__(self, e, i):
        self.e = e
        self.i = i


def solve(a, k):
    animals = [Animal(e, i + 1) for i, e in enumerate(a)]
    animals.sort()

    i = 0
    while i < len(animals) and k > 0:
        m = 1
        e = animals[i].e
        while i + m < len(animals) and animals[i + m].e == e:
            m += 1

        d = (len(animals) - i) * m
        
        k -= d
        i += m
        for j in range(i, len(animals)):
            animals[j] -= e


    if not animals:
        return [-1]

    i = 0
    k = k % n
    while k > 0:
        a = animals[i]
        a.e -= 1
        if a.e == 0:
            animals.pop(i)
            if not animals:
                return [-1]
        else:
            i += 1
        if i >= len(animals):
            i = 0

        k -= 1

    result = []
    for j in range(len(animals)):
        result.append(animals[i].i)
        i = (i + 1) % len(animals)
    return result


def num_input():
    return map(int, raw_input().split(' '))


if 'test' in sys.argv:
    assert(solve([1, 2, 1], 3) == [2])
    assert(solve([3, 3, 2, 1], 10) == [-1])
    assert(solve([1, 3, 3, 1, 2, 3, 1], 10) == [6, 2, 3])
else:
    n, k = num_input()
    a = num_input()
    print ' '.join(map(str, solve(a, k)))

