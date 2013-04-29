class Graph(object):
	def __init__(self, size, directed=False):
		self.directed = directed
		self.matrix = [[False] * size for x in range(size)]

	def __len__(self):
		return len(self.matrix)

	def addEdge(self, v1, v2):
		self.matrix[v1][v2] = True
		if self.directed:
			self.matrix[v2][v1] = True

	def adjacent(self, v1):
		m = self.matrix[v1]
		for v2 in range(len(self)):
			if m[v2]:
				yield v2


class ImGraph(object):

	def __init__(self, vertexCount, maxEdgeCount):
		self.matrix = [[False] * maxEdgeCount for v in range(vertexCount)]
		self.edgeCount = 0
		
	def addEdge(self, v1, v2):
		self.matrix[v1][self.edgeCount] = True
		self.matrix[v2][self.edgeCount] = True
		self.edgeCount += 1

	def adjacent(self, v):
		n = len(self.matrix)
		edges = self.matrix[v]
		for i in range(self.edgeCount):
			if not edges[i]:
				continue
			for v2 in range(n):
				if v2 != v and self.matrix[v2][i]:
					yield v2