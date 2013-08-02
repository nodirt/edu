from nums import *

p = 0
q = []
limit = 10 ** 6
max_len = 0
max_p = 0


ps = list(primes(10000))
for i in range(len(ps)):
    p = 0
    for j in range(i, len(ps)):
        p += ps[j]
        if p >= limit:
            break
        ln = j - i + 1
        if ln > max_len and is_prime(p):
            max_len = ln
            q = ps[i:j]
            max_p = p

print(max_p)
print(q)