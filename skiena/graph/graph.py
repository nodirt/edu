import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from datastruct.queue import Queue
from datastruct.stack import Stack
from util.enum import enum
from graphMatrix import Graph as MGraph

class EdgeNode(object):
	def __init__(self, vertex, weight=0, next=None):
		self.vertex = vertex
		self.weight = weight
		self.next = next

VertexState = enum('VertexState', 'undiscovered', 'discovered', 'processed')

class Vertex(object):
	def __init__(self, label=None):
		self.label = label
		self.edgeHead = EdgeNode(None)
		self.degree = 0

	def addEdge(self, vertex, weight=0, checkDup=False):
		if not checkDup:
			node = EdgeNode(vertex, weight)
			node.next = self.edgeHead.next
			self.edgeHead.next = node
		else:
			n = self.edgeHead
			while n.next:
				if n.next.vertex == vertex:
					return
				n = n.next
			n.next = EdgeNode(vertex, weight)
		self.degree += 1

	def __str__(self):
		return str(self.label)

	def removeEdge(self, vertex):
		n = self.edgeHead
		while n.next:
			if n.next.vertex == vertex:
				n.next = n.next.next
				break
			n = n.next

	def adjacent(self):
		result = []
		n = self.edgeHead.next
		while n:
			result.append(n.vertex)
			n = n.next
		return result


class Graph(object):
	def __init__(self, size=0, directed=False, labels=None):
		self.directed = directed
		if not labels:
			labels = [str(i + 1) for i in range(size)]
		self.vertexes = [Vertex(l) for l in labels]

	def label(self, vertex):
		return self.vertexes[vertex].label

	def __iter__(self):
		for v in self.vertexes:
			yield v.label

	def __getitem__(self, vertex):
		return self.label(vertex)

	def __setitem__(self, vertex, label):
		self.vertexes[vertex].label = label

	def adjacent(self, vertex):
		return self.vertexes[vertex].adjacent()

	def addEdge(self, v1, v2):
		self.vertexes[v1].addEdge(v2, checkDup=not self.directed)
		if not self.directed:
			self.vertexes[v2].addEdge(v1, checkDup=True)

	def __len__(self):
		return len(self.vertexes)

	@staticmethod
	def read(inFile, directed):
		n = int(inFile.readline())
		g = Graph(n, directed)
		for v in range(n):
			for j in inFile.readline().split(' '):
				v2 = int(j) - 1
				g.addEdge(v, v2)
		return g

	def dump(self):
		n = len(self.vertexes)
		print(n)
		for v in range(n):
			adjacent = ' '.join(map(lambda v: str(self.label(v)), self.adjacent(v)))
			print('%s: %s' % (self.label(v), adjacent))

	def bfs(self, processVertexEarly=None, processEdge=None, processVertexLate=None, root=0):
		if not self.vertexes:
			return

		state = [VertexState.undiscovered] * len(self)
		state[root] = VertexState.discovered
		parents = [-1] * len(self)
		result = BfsResult(parents)

		q = Queue([root])
		while q:
			v = q.dequeue()

			if processVertexEarly and processVertexEarly(v) == False:
				result.interupted = True
				break
			state[v] = VertexState.processed

			for v2 in self.adjacent(v):
				if processEdge and (state[v2] != VertexState.processed or self.directed) and processEdge(v, v2) == False:
					result.interupted = True
					break

				if state[v2] == VertexState.undiscovered:
					parents[v2] = v
					state[v2] = VertexState.discovered
					q.enqueue(v2)

			if processVertexLate and not processVertexLate(v):
				result.interupted = True
				break

		return result

	def connectedComponents(self):
		components = []
		n = len(self)
		visited = [False] * n

		def visitVertex(v):
			visited[v] = True
			curComponent.append(v)

		for v in range(n):
			if visited[v]:
				continue
			curComponent = []
			self.bfs(visitVertex, root=v)
			components.append(curComponent)
		return components

	def colorCount(self):
		n = len(self)
		color = [0] * n
		maxColor = [0]


		def visitVertex(v1):
			adjColors = []
			for v2 in self.adjacent(v1):
				if color[v2] != 0:
					adjColors.append(color[v2])
			c = 1
			adjColors.sort()
			for c2 in adjColors:
				if c2 > c:
					break
				elif c == c2:
					c += 1

			color[v1] = c
			maxColor[0] = max(maxColor[0], c)

		for v in range(n):
			if color[v] != 0:
				continue
			color[v] = 1
			self.bfs(visitVertex, root=v)
		return maxColor[0]

	def bipartite(self):
		return self.colorCount() == 2

	def dfs(self, processVertexEarly=None, processEdge=None, processVertexLate=None, root=0):
		if not self.vertexes:
			return

		n = len(self)
		state = [VertexState.undiscovered] * n
		time = [None] * n
		parents = [-1] * n
		result = DfsResult(parents, time)
		timer = [0]

		def search(v):
			start = timer[0]
			timer[0] += 1
			if processVertexEarly and processVertexEarly(v) == False:
				return False
			state[v] = VertexState.discovered

			for v2 in self.adjacent(v):
				s2 = state[v2]
				if s2 == VertexState.undiscovered:
					parents[v2] = v
				if s2 != VertexState.processed and processEdge(v, v2, s2 == VertexState.discovered) == False:
					return False
				if s2 == VertexState.undiscovered and not search(v2):
					return False
			time[v] = (start, timer[0])
			timer[0] += 1

			if processVertexLate and not processVertexLate(v):
				return False

			state[v] = VertexState.processed
			return True

		result.interupted = not search(root)
		return result

	def isCyclic(self):
		def visitEdge(v1, v2, back):
			return not back
		return self.dfs(processEdge=visitEdge).interupted

	def eval(self, root):
		cache = [None] * len(self)

		def eval0(v):
			val = self.vertexes[v].label
			if type(val) in (int, float):
				return float(val)

			if cache[v] is not None:
				return cache[v]
			right, left = [eval0(v2) for v2 in self.adjacent(v)]
			if val == '+':
				result = left + right
			elif val == '-':
				result = left - right
			elif val == '*':
				result = left * right
			elif val == '/':
				result = left / right
			else:
				raise ValueError('Unkown operator: %s' % val)
			cache[v] = result
			return result

		return eval0(root)

	def graph2(self):
		g2 = Graph(labels=self, directed=self.directed)
		seen = [0] * len(self)
		def visit(v, p):
			seen[v] += 1
			for v2 in self.adjacent(v):
				if p is not None and v2 != p:
					g2.vertexes[p].addEdge(v2, checkDup=True)
				if seen[v2] < 2:
					visit(v2, v)

		visit(0, None)		
		return g2

class SearchResult(object):
	def __init__(self, parents):
		self.interupted = False
		self.parents = parents

class BfsResult(SearchResult):
	def findShortest(self, to):
		path = Stack()
		while to >= 0:
			path.push(to)
			to = self.parents[to]
		return path

class DfsResult(SearchResult):
	def __init__(self, parents, time):
		SearchResult.__init__(self, parents)
		self.time = time


def printLabel(v):
	print('Vertex %s' % v)


def printEdge(a, b):
	print('Edge %s-%s' % (a, b))

def printEdgeDfs(a, b, back):
	print('Edge %s-%s%s' % (a, b, '. Back edge' if back else ''))

def main():
	with open('graph.in') as inData:
		g = Graph.read(inData, False)
	print('Dump:')
	g.dump()

	print('\nBFS:')
	bfs = g.bfs(printLabel, printEdge)

	print('\nParents:')
	for v in range(len(g)):
		p = bfs.parents[v]
		if p:
			print('%s: %s' % (v, p))
		else:
			print('%s has no parent' % v)

	print('\nShortest paths:')
	for v in range(len(g)):
		path = map(g.label, bfs.findShortest(v))
		print('%s: %s' % (v, ' '.join(path)))

	print('\nConnected components:')
	for c in g.connectedComponents():
		print(' '.join(map(g.label, c)))

	assert(g.colorCount() == 4)

	def bintree(directed=False):
		bintree = Graph(4, directed)
		bintree.addEdge(0, 1)
		bintree.addEdge(0, 2)
		bintree.addEdge(1, 3)
		return bintree
	assert(bintree().colorCount() == 2)

	assert(Graph(1).colorCount() == 1)
	assert(Graph(0).colorCount() == 0)

	print('\nDFS:')
	dfs = g.dfs(printLabel, printEdgeDfs)
	print('Times from 0:')
	for v in range(len(g)):
		if dfs.time[v]:
			s, e = dfs.time[v]
			print('%s: %s-%s' % (v, s, e))

	# Cycle detection
	assert(g.isCyclic())
	assert(not bintree(True).isCyclic())


	mg = MGraph(len(g), False)
	for v in range(len(g)):
		for v2 in g.adjacent(v):
			mg.addEdge(v, v2)

	print('\nExpression evaluation:')
	expr = Graph(labels=['+', '+', 2, '*', 3, 4, '/', 5], directed=True)
	expr.addEdge(0, 1)
	expr.addEdge(0, 6)
	expr.addEdge(1, 2)
	expr.addEdge(1, 3)
	expr.addEdge(2, 3)
	expr.addEdge(3, 4)
	expr.addEdge(3, 5)
	expr.addEdge(6, 3)
	expr.addEdge(6, 7)
	expr.dump()
	print(expr.eval(0))

	# graph2
	g7 = Graph(7, directed=True)
	g7.addEdge(0, 1)
	g7.addEdge(1, 2)
	g7.addEdge(1, 4)
	g7.addEdge(2, 3)
	g7.addEdge(3, 6)
	g7.addEdge(4, 3)
	g7.addEdge(4, 5)
	g7.addEdge(6, 5)
	g7.dump()

	g72 = g7.graph2()
	g72.dump()
	def setassert(a, b):
		assert(set(a) == set(b))
	setassert(g72.adjacent(0), (2, 4))
	setassert(g72.adjacent(1), (3, 5))
	setassert(g72.adjacent(2), (6,))
	setassert(g72.adjacent(3), (5,))
	setassert(g72.adjacent(4), (6,))
	setassert(g72.adjacent(5), ())

if __name__ == '__main__':
	main()