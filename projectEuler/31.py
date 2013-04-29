amounts = [1, 2, 5, 10, 20, 50, 100, 200]
amounts.reverse()

def combinations(sum, startAt=0):
    if startAt >= len(amounts):
        return 0
    elif startAt == len(amounts) - 1:
        return 1

    result = 0
    while sum > 0:
        result += combinations(sum, startAt + 1)
        sum -= amounts[startAt]
    if sum == 0:
        result += 1
    return result

for i in range(1, 20):
    print(i, combinations(i))
print(200, combinations(200))