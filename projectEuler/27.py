import nums
primes = set(nums.primes(1000))

def primeCount(a, b):
    n = 0
    while True:
        if (n * n + a * n + b) not in primes:
            break
        n += 1
    return n


results = [((a, b), primeCount(a, b)) for b in primes for a in range(-b, 1000, 2)]
a, b = max(results, key=lambda t: t[1])[0]
print(a, "*", b, "=", a * b)
print("Makes %s primes" % primeCount(a, b))