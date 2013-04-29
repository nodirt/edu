from math import factorial
from nums import digits

digFac = [factorial(x) for x in range(10)]

result = 0
for x in range(10, 10 ** 6):
    if x == sum(digFac[d] for d in digits(x)):
        print(x)
        result += x

print('Sum:', result)
