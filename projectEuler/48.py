import math

size = 10

class DigNum(object):
	def __init__(self, x=0):
		d = [0] * size

		i = 0
		while x > 0 and i < size:
			d[i] = x % 10
			x /= 10
			i += 1

		self.d = d

	def __getitem__(self, i):
		return self.d[i]

	def __setitem__(self, i, d):
		self.d[i] = d % 10

	def __mut(self, func):
		r = 0
		for i in xrange(size):
			x = func(i) + r
			self.d[i] = x % 10
			r = x / 10

	def __add__(self, other):
		result = DigNum()
		result.__mut(lambda i: self[i] + other[i])
		return result

	def __mul__(self, other):
		result = DigNum()
		if type(other) == int:
			result.__mut(lambda i: self[i] * other)
		elif type(other) == DigNum:
			for x in reversed(self.d):
				result.d.pop(-1)
				result.d.insert(0, 0)
				if x > 0:
					result += other * x
		else:
			raise Error('Cannot multiply by %s' % type(other))
		return result

	def __pow__(self, other):
		if other == 0:
			return DigNum(1)
		elif other == 1:
			return self

		half = int(math.floor(other / 2))
		result = self ** half
		result = result * result
		rest = other - half * 2
		if rest > 0:
			result *= pow(self, rest)
		return result


	def __int__(self):
		x = 0
		for i in range(size - 1, -1, -1):
			x = x * 10 + self.d[i]
		return x


def test():
	assert(int(DigNum(123)) == 123)
	assert(int(DigNum(1123131231234567890)) == 1234567890)
	assert(int(DigNum(123) + DigNum(34)) == 157)
	assert(int(DigNum(43) * 314) == 43 * 314)
	assert(int(DigNum(13) * DigNum(34)) == 13 * 34)
	assert(int(DigNum(3) ** 5) == 3 ** 5)


def solve():
	x = DigNum()
	for i in range(1, 1001, 1):
		x += DigNum(i) ** i
	return int(x)

if __name__ == '__main__':
	print(solve())