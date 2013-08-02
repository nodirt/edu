from itertools import count, takewhile

def makeNum(digs, start=0, end=None):
    if end is None:
        end = len(digs)
    x = 0
    for i in range(start, end):
        x *= 10
        x += digs[i]
    return x

def digits(x):
    while x:
        x, d = divmod(x, 10)
        yield d

def isPrime(x):
    if x < 2:
        return False
    half = x // 2
    if _primes and _primes[-1] >= half:
        delimeters = takewhile(lambda x: x <= half, _primes)
    else:
        delimeters = range(2, half + 1)
    for y in delimeters:
        if x % y == 0:
            return False
    return True

def is_prime(x):
    return isPrime(x)

_primes = [2, 3]
def primes(maxPrime=None):
    for p in _primes:
        if maxPrime is not None and p > maxPrime:
            return
        yield p

    x = _primes[-1] + 2
    while maxPrime is None or x <= maxPrime:
        isPrime = True
        for p in _primes:
            if x % p == 0:
                isPrime = False
                break
        if isPrime:
            _primes.append(x)
            yield x
        while True:
            x += 2
            if x % 10 not in (0, 5):
                break

def is_perm(x, y):
    d = [0] * 10

    while x > 0:
        d[x % 10] += 1
        x /= 10


    while y > 0:
        d[y % 10] -= 1
        y /= 10

    return all(c == 0 for c in d)


def palindroms():
    for dc in count(1):
        odc = dc // 2
        for h in range(10 ** (odc - 1), 10 ** odc) if odc else [0]:
            for t in range(10) if dc % 2 else [None]:
                x = h
                if t is not None:
                    x = x * 10 + t
                for d in digits(h):
                    x = x * 10 + d
                yield x

