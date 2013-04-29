import itertools
import math
import queue
import nums

heads = queue.Queue()
for h in [2, 3, 5, 7]:
    heads.put(h)

result = 0
resultCount = 0
p10 = 1
while resultCount < 11:
    h = heads.get() * 10
    while h > p10:
        p10 *= 10
    p10 //= 10
    
    for t in range(1, 10, 2):
        x = h + t
        if not nums.isPrime(x):
            continue
        heads.put(x)

        p = p10
        y = x
        good = True
        while p > 1:
            y %= p
            if not nums.isPrime(y):
                good = False
                break
            p //= 10
        if good:
            result += x
            resultCount += 1
            print(x)

print('Sum:', result)