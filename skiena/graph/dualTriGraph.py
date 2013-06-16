def dualGraph(triangles, vertexCount):
    n = len(triangles)
    index = [[] for v in range(vertexCount)]
    for t in range(n):
        for v in triangles[t]:
            index[v].append(t)
    print(index)

    adjList = []
    for t in range(n):
        v1, v2, v3 = triangles[t]
        adj = []
        for t2 in index[v1]:
            if t2 != t and any(vt == v2 or vt == v3 for vt in triangles[t2]):
                adj.append(t2)
        for t2 in index[v2]:
            if t2 != t and t2 not in adj and any(vt == v1 or vt == v3 for vt in triangles[t2]):
                adj.append(t2)

        adjList.append(adj)
    return adjList

triangles = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [3, 5, 7], [5, 6, 8]]
for i, adj in enumerate(dualGraph(triangles, 10)):
    adjStr = ' '.join(str(a + 1) for a in adj)
    print('%s: %s' % (i + 1, adjStr))