nums = set()
for a in range(2, 101):
    x = a
    for b in range(2, 101):
        x *= a
        nums.add(x)

print(len(nums))
