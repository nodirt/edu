import math

fib = [1, 1, 2]
i = 2
index = 3
maxPower = 999

while int(math.log10(fib[i])) < maxPower:
    index += 1
    i += 1
    if i > 2:
        i = 0
    fib[i] = fib[i - 2] + fib[i - 1]


print(index)
