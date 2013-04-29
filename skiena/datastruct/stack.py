class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class Stack(object):
	def __init__(self, items=None):
		self.first = None
		self.size = 0
		if items:
			for x in items:
				self.push(x)

	def __len__(self):
		return self.size

	def push(self, value):
		node = Node(value)
		node.next = self.first
		self.first = node
		self.size += 1
		return self

	def peek(self):
		if not self.first:
			raise ValueError('Stack is empty')
		return self.first.value

	def pop(self):
		if not self.first:
			raise ValueError('Stack is empty')
		value = self.first.value
		self.first = self.first.next
		self.size -= 1
		return value

	def __iter__(self):
		n = self.first
		while n:
			yield n.value
			n = n.next

if __name__ == '__main__':
	s = Stack()
	assert(not s)
	s.push(1).push(2).push(3)
	assert(list(s) == [3, 2, 1])
	assert(len(s) == 3)
	assert(s)
	assert(s.peek() == 3)

	assert(s.pop() == 3)
	assert(len(s) == 2)
	assert(s.peek() == 2)

	assert(s.pop() == 2)
	assert(s.pop() == 1)
	assert(len(s) == 0)
	assert(not s)

	print('All tests pass')
