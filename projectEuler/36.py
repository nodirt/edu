from itertools import takewhile, dropwhile
from nums import palindroms

result = 0

for x in takewhile(lambda x: x < 10 ** 6, palindroms()):
    b = bin(x)[2:]
    if all(b[i] == b[-1 - i] for i in range(len(b) // 2)):
        print("%d -- %s" % (x, b))
        result += x

print('Sum:', result)