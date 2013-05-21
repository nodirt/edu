def dec(x):
	d1p = 10
	while True:
		d1 = int(x // d1p) % 10

		d2p = 1
		found = False
		while d2p < d1p:
			d2 = int(x // d2p) % 10
			if d2 < d1:
				found = True
				break
			d2p *= 10

		if found:
			break

		d1p *= 10

	x -= d1p * (d1 - d2)
	x += d2p * (d1 - d2)

	y = int(x // d1p) * d1p

	# 4123 -> (43) -> 3124 -> 3421
	# 4312 -> (32) -> 4213 -> 4231
	# 2134 -> (21) -> 1234 -> 1432
	big = int(d1p // 10)
	small = 1
	while big > 0:
		d = int(x // big) % 10
		y += d * small
		small *= 10
		big = int(big // 10)

	return y

def isPrime(x):
	for y in range(2, x // 2):
		if x % y == 0:
			return False
	return True

def printPrime(x):
	while True:
		if isPrime(x):
			print(x)
			return True

		px = x
		x = dec(x)
		if px == x:
			break

	return False

printPrime(7654321)