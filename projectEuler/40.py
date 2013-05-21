p10 = [10 ** k for k in range(10)]

b = [0] * 10
for k in range(1, len(b)):
	b[k] = b[k - 1] + k * 9 * p10[k - 1]

k = 0
result = 1
for p in range(7):
	i = p10[p]
	while i >= b[k + 1]:
		k += 1
	j = i - b[k] - 1
	x = int(p10[k] + j / (k + 1))
	d = int(x // p10[k - j % (k + 1)]) % 10
	# print('d[%d] = %d' % (p10[p], d))
	result *= d

print(result)