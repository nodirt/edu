from fractions import Fraction as frac

result = frac(1)

for a in range(11, 99):
    if a % 10 == 0:
        continue
    a0, a1 = divmod(a, 10)

    for b in range(a + 1, 99):
        if b % 10 == 0:
            continue
        f = frac(a, b)
        
        b0, b1 = divmod(b, 10)
        if a0 == b1 and f == frac(a1, b0) or a1 == b0 and f == frac(a0, b1):
            result *= f
            print('%d/%d = %s' % (a, b, f))

print('Product:', result)            