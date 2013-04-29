class Tree(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def eval(expr):
	v = expr.value
	if type(v) == int:
		return expr.value

	l = eval(expr.left)
	r = eval(expr.right)

	if v == '+':
		return l + r
	elif v == '-':
		return l - r
	elif v == '*':
		return l * r
	elif v == '/':
		return l / r
	else:
		raise ValueError('Unknown value: %s' % v)


