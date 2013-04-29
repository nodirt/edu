from nums import digits

power = 5

result = 0

pdig = [x ** power for x in range(10)]

for x in range(10, 10 ** 7):
    s = 0
    for dig in digits(x):
        s += pdig[dig]
        if s > x:
            break
    if s == x:
        result += x
        print(x)

print("Sum: ", result)