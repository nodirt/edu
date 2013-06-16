import math
import nums

def check(x, factorCount):
    def all_uniq(x):
        count = 0
        for p in nums.primes(x):
            if x % p != 0:
                continue
            x /= p
            while x % p == 0:
                x /= p
            count += 1
            if count == factorCount:
                return x == 1
            elif x == 1:
                return False
        assert(False)

    return all(all_uniq(x + i) for i in xrange(factorCount))
                
def solve(factorCount):
    x = 2
    while True:
        if check(x, factorCount):
            return x
        x += 1

print(solve(4))
