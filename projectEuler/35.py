from nums import isPrime

pow10 = [10 ** x for x in range(7)]

result = 0
c = []
digCount = 1
digCountEdge = pow10[digCount]
p = pow10[digCount - 1]
for x in range(2, 10 ** 6):
    if x >= digCountEdge:
        digCount += 1
        digCountEdge = pow10[digCount]
        p = pow10[digCount - 1]

    if x != 2:
        skip = True
        y = x
        del c[0:len(c)]
        while True:
            y, d = divmod(y, 10)
            if d % 2 == 0:
                break
            y += d * p
            if y < x:
                break
            elif y == x:
                skip = False
                break
            c.append(y)

        if skip:
            continue

    if isPrime(x) and all(isPrime(x) for x in c):
        c.insert(0, x)
        print(c)
        result += len(c)

print(result)