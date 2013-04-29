import sys

class Book:
	def __init__(self, t, w):
		self.t = t
		self.w = w


def compareBooksReverse(a, b):
	if a.w != b.w:
		return b.w - a.w
	return b.t - a.t

def solve(bs):
	bs = list(bs)
	bs.sort(compareBooksReverse)

	width = sum(b.w for b in bs)
	thickness = 0
	for b in bs:
		thickness += b.t
		width -= b.w
		if thickness >= width:
			break
	return thickness


if 'test' in sys.argv:
	bs = [Book(1, 12), Book(1, 3), Book(2, 15), Book(2, 5), Book(2, 1)]
	assert(solve(bs) == 5)

	bs = [Book(1, 10), Book(2, 1), Book(2, 4)]
	assert(solve(bs) == 3)
else:
	n = input()
	bs = []
	for i in range(n):
		ts, ws = raw_input().split(' ')
		bs.append(Book(int(ts), int(bs)))
	print solve(bs)