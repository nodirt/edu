nums = [1, 2, 3, 5, 7, 11, 13, 17]

def solve(digits, level, suffix):
	divisor = nums[level]
	if divisor == 1:
		for d in digits:
			if d != 0:
				yield d
		return
	
	if divisor == 2 and suffix % 2 != 0:
		return 

	for d in digits:
		p = d * 100 + suffix
		if p % divisor != 0:
			continue

		digits.remove(d)
		newSuffix = d * 10 + suffix // 10
		for pd in solve(digits, level - 1, newSuffix):
			yield pd * 10 + d
		digits.add(d)

def dividedBy(x):
	y = 100 // x
	while x * y < 1000:
		p = x * y
		y += 1
		if p < 100:
			continue
		yield p

def findAll():
	for x17 in dividedBy(17):
		d8 = int(x17 // 100)
		d9 = int(x17 // 10) % 10
		d10 = x17 % 10
		if d8 == d9 or d8 == d10 or d9 == d10:
			continue
		digits = set(range(10)) - set((d8, d9, d10))
		# print(digits)
		suffix = x17 // 10
		for prefix in solve(digits, len(nums) - 2, suffix):
			yield prefix * 1000 + x17

print(sum(findAll()))