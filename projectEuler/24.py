from math import factorial as fac

x = 999999
count = 10

result = []
digits = list(range(count))
while x:
    permCount = fac(len(digits) - 1)
    result.append(digits.pop(x // permCount))
    x %= permCount
result += digits
print(''.join(map(str, result)))