def divide(a, b):
	if b > a:
		return (0, a)
	elif b == a:
		return (1, 0)

	c, a = divide(a, b + b)
	c += c

	while b <= a:
		a -= b
		c += 1

	return (c, a)


for x in range(0, 1000):
	for y in range(1, 1000):
		assert(divide(x, y)[0] == x // y)